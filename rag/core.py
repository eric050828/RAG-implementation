import os
from pathlib import Path
from urllib.parse import urlparse

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    WebBaseLoader,
    UnstructuredPowerPointLoader,
)
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate


load_dotenv("./.config/.env")
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError("OpenAI API key not found.")
os.environ["OPENAI_API_KEY"] = api_key

VECTORDB_DIRECTORY = "vectordb"
LLM = ChatOpenAI(
    model="gpt-3.5-turbo",
    streaming=True,
    # callbacks=[StreamingStdOutCallbackHandler()],
    temperature=0
)
EMBEDDING = OpenAIEmbeddings()
name = ""
vectordb = None
prompt = PromptTemplate(
        input_variables=["history", "context", "question"],
        template="You are a very powerful assistant for question-answering tasks.\n  Please use the retrieved context pieces to answer the questions, step-by-step reasoning and inference to provide deeper and more accurate information.\nIf you don't know the answer, simply say you don't know to avoid uncertain or inaccurate results.\nEnsure that your responses are based on reliable sources, comprehensive data retrieval, and known information.\nContext:{context}\nhistory:{history}\nquestion:{question}\nAnswer:",
    )

memory = ConversationBufferMemory(
    memory_key="history",
    input_key="question"
)

def _load_pdf(
        path: str, 
        password: str | bytes | None = None,
        extract_images: bool = False,):
    loader = PyPDFLoader(
        file_path=path,
        password=password,
        extract_images=extract_images
    )
    data = loader.load()
    return data

def _load_txt(
        path: str,):
    loader = TextLoader(
        file_path=path,
        autodetect_encoding=True
    )
    data = loader.load()
    return data

def _load_web(
        path: str):
    loader = WebBaseLoader(
        web_path=path,
    )
    data = loader.load()
    return data

def _load_pptx(
        path: str,):
    loader = UnstructuredPowerPointLoader(
        file_path=path,
        mode="elements"
    )
    data = loader.load()
    return data

def _split(
        data):
    splitter = RecursiveCharacterTextSplitter(chunk_size=2000)
    chunks = splitter.split_documents(data)
    return chunks

def _get_path_name(
        path: str):
    if path.startswith(("http://", "https://", "www.")):
        parsed_url = urlparse(path)
        return parsed_url.netloc.replace(".", "-")[:64]
    path = Path(path)
    return path.name

def save(
        path: str):
    global name, vectordb
    name = _get_path_name(path)
    if path.startswith(("http://", "https://", "www.")):
        data = _load_web(path)
    else:
        path = Path(path)
        match path.suffix:
            case ".pdf":
                data = _load_pdf(path)
            case ".txt":
                data = _load_txt(path)
            case ".pptx":
                data = _load_pptx(path)
            case _:
                return False
    chunks = _split(data)
    vectordb = Chroma.from_documents(
            collection_name=name, 
            documents=chunks, 
            embedding=EMBEDDING, 
            persist_directory=VECTORDB_DIRECTORY, 
        )
    # vectordb.persist()
    
def saves(
        paths: list[str],):
    for path in paths:
        save(path)

def get_response(
        path: str,
        question: str,
        history: list[str],):
    save(path)
    retriever = vectordb.as_retriever(search_kwargs={"k":4})

    retrieval_qa_chain = RetrievalQA.from_chain_type(
        LLM,
        chain_type='stuff',
        retriever=retriever,
        chain_type_kwargs={
            "prompt": prompt,
            "memory": memory,
        }
    )
    return retrieval_qa_chain.run(question)