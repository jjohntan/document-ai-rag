# Document-AI — PDF Question Answering System

Built an end-to-end RAG application that allows users to upload PDF documents and ask questions about their contents. The system extracts and chunks document text, generates embeddings, stores them in a vector database, retrieves relevant context through semantic search, and uses an LLM to generate grounded answers

## 🚀 Installation

```bash
git clone https://github.com/jjohntan/document-ai-rag
cd document-ai-rag
```

## 📦 Dependensies

```bash
python -m venv .venv
source .venv/bin/activate    # Linux

pip install -r requirements.txt
```

### Run the program

```bash
python -m streamlit run src/app.py
```

### 📁 File structure

```bash
document-ai-rag/
├── src/
│   ├── app.py
│   ├── chunking.py
│   ├── gen_prompt.py
│   ├── parser.py
│   └── vector_store.py
├── .env
├── README.md 
└── requirements.txt
```

![alt text](image/Demo.png)
![alt text](image/Result.png)

### Reference
https://docs.python.org/3/library/argparse.html#type
https://academy.claude.com/courses/building-with-the-claude-api/text-chunking-strategies
https://sbert.net/
https://huggingface.co/sentence-transformers
https://www.reddit.com/r/Rag/comments/1i5rpyd/for_an_absolute_beginner_which_is_the_vector/
https://medium.com/@yashpaliwal42/simple-rag-retrieval-augmented-generation-implementation-using-faiss-and-openai-2a74775b17c3
https://hackernoon.com/build-a-vector-search-engine-in-python-with-faiss-and-sentence-transformers
https://medium.com/@aymen.besbes/build-your-first-retrieval-augmented-generation-rag-system-with-faiss-sentence-transformers-and-200a8db91517
https://medium.com/@kaviyadharishini21/retrievers-the-backbone-of-retrieval-augmented-generation-1544f34dd459