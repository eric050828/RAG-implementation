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
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings


load_dotenv("./.config/.env")
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError("OpenAI API key not found.")
os.environ["OPENAI_API_KEY"] = api_key

VECTORDB_DIRECTORY = "vectordb"


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
    )
    data = loader.load()
    return data

def _split(
        data):
    splitter = RecursiveCharacterTextSplitter()
    chunks = splitter.split_documents(data)
    return chunks

def save(
        path: str):
    if path.startswith(("http://", "https://", "www.")):
        parsed_url = urlparse(path)
        name = parsed_url.netloc + parsed_url.path
        _load_web(path)
    else:
        path = Path(path)
        name = path.name
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
            embedding=OpenAIEmbeddings(), 
            persist_directory=VECTORDB_DIRECTORY, 
        )
    vectordb.persist()
    
def saves(
        paths: list[str],):
    for path in paths:
        save(path)