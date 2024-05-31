# Chat with Docs
>能夠讓AI在讀取你的資料後來回答你的問題，完美解決以前AI在沒有使用者提供資料的情況下胡言亂語的情況
## 有哪些模型可以使用？
目前支援了**OpenAI**和**Gemma**
## 部屬前提
如需使用Gemma請參閱[Ollama官方文檔](https://ollama.com/library/gemma)安裝及部屬並確保下列指令能夠正常使用
```
ollama run gemma
>>> Send a message (/? for help)
```
## 如何部屬
### Clone
如未安裝git可使用[此連結](https://github.com/l0sscat/RAG-implementation/archive/refs/heads/main.zip)下載至本地並解壓縮執行

若本機有安裝git可使用下列指令將此專案下載至本地
```
git clone https://github.com/l0sscat/RAG-implementation.git
```
### 環境設置
如需使用OpenAI需於`.config/.env`內將`OPENAI_API_KEY`設置API Key

建議使用Python的虛擬環境來建立該專案
```
python -m venv .venv        #建立虛擬環境
.venv\Scripts\activate      #開啟虛擬環境
```
安裝所需套件
```
pip install -r requirements.txt
```
### 執行
```
streamlit run main.py
```