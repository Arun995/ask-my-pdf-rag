# AskMyPDF — RAG-Based PDF Question Answering Bot

A Retrieval-Augmented Generation (RAG) application that allows users to upload a PDF document and ask questions about its contents using natural language.

The application processes the uploaded document, converts its content into searchable vector embeddings, retrieves relevant document sections, and uses a large language model to generate an answer based on the retrieved information.

## Features

- Upload a PDF document
- Automatically process and split the document into smaller text chunks
- Generate vector embeddings for document chunks
- Store document embeddings in a persistent Chroma vector database
- Retrieve relevant document content based on the user's question
- Generate answers using an LLM through Groq
- Interactive Streamlit user interface
- Supports natural-language questions about uploaded documents

## Tech Stack

- Python
- Streamlit
- LangChain
- LangChain Community
- LangChain Text Splitters
- Hugging Face Embeddings
- Chroma
- Groq
- PyPDFLoader
- Retrieval-Augmented Generation (RAG)
- python-dotenv

## How It Works

The application follows a Retrieval-Augmented Generation pipeline.

PDF Upload
    ↓
PDF Document Loader
    ↓
Text Extraction
    ↓
Text Chunking
    ↓
Hugging Face Embeddings
    ↓
Chroma Vector Database
    ↓
User Question
    ↓
Similarity-Based Retrieval
    ↓
Retrieved Document Context
    ↓
Large Language Model
    ↓
Generated Answer

## RAG Pipeline

### 1. PDF Upload

The user uploads a PDF document through the Streamlit interface.

The application accepts PDF files using Streamlit's file uploader.

### 2. Document Loading

The uploaded PDF is loaded using PyPDFLoader.

The extracted document content is then passed to the text-processing pipeline.

### 3. Text Splitting

The extracted document is divided into smaller chunks using RecursiveCharacterTextSplitter.

Configuration used in the project:

- Chunk size: 2000 characters
- Chunk overlap: 200 characters

The overlap helps preserve contextual information between neighboring chunks.

### 4. Embedding Generation

Each document chunk is converted into a numerical vector representation using Hugging Face Embeddings.

These embeddings allow the application to perform semantic similarity-based retrieval.

### 5. Vector Storage

The generated embeddings and document chunks are stored in a persistent Chroma vector database.

The vector database is stored locally in the doc_vectorstore directory.

### 6. Question Retrieval

When the user enters a question, the application uses the Chroma vector database as a retriever to find relevant document content.

Only the retrieved content is passed to the question-answering chain as contextual information.

### 7. Answer Generation

The retrieved document context is provided to the configured language model through LangChain's RetrievalQA chain.

The project uses the following Groq model:

openai/gpt-oss-120b

The model is configured with temperature set to 0 to produce more deterministic responses.

## Project Structure

pdf-qa-rag/
│
├── app.py
├── rag_utility.py
├── requirements.txt
├── .env
│
└── doc_vectorstore/
    └── Chroma vector database files

## Main Components

### app.py

The Streamlit application responsible for:

- Displaying the user interface
- Accepting PDF uploads
- Saving the uploaded PDF
- Processing the uploaded document
- Accepting user questions
- Displaying generated answers

### rag_utility.py

Contains the main RAG functionality, including:

- PDF loading
- Text splitting
- Embedding generation
- Chroma vector database creation
- Retriever configuration
- RetrievalQA chain
- LLM configuration

## Installation

Clone the repository and navigate into the project directory.

Install the required Python packages:

pip install -r requirements.txt

Create a .env file and add the required Groq API key.

Example:

GROQ_API_KEY=your_api_key_here

## Running the Application

Run the Streamlit application using:

streamlit run app.py

After starting the application, open the Streamlit URL shown in the terminal.

Upload a PDF and enter a question about its contents.

## Example Usage

1. Launch the application.
2. Upload a PDF document.
3. Wait for the document to be processed.
4. Enter a question related to the document.
5. Click the Answer button.
6. The application retrieves relevant document content and generates an answer.

Example questions:

- What is the main topic of this document?
- Summarize the key points.
- What does the document say about a specific topic?
- Explain a particular section.
- What conclusions are presented in the document?

## Key Concepts Demonstrated

This project demonstrates practical implementation of:

- Retrieval-Augmented Generation (RAG)
- Document loading
- Text chunking
- Semantic search
- Vector embeddings
- Vector databases
- Information retrieval
- Large Language Models
- LangChain pipelines
- Streamlit application development

## Configuration

The application uses environment variables for sensitive configuration.

The .env file should not be committed to GitHub.

Add .env to .gitignore before pushing the project to a public repository.

Example .gitignore:

.env
__pycache__/
*.pyc

## Limitations

- The application currently works with PDF documents.
- The vector database is stored locally.
- The application processes one uploaded document at a time.
- Answer quality depends on the retrieved document context and language model.
- Very large documents may require additional optimization for efficient processing.

## Future Improvements

- Add support for multiple document formats
- Support multiple PDFs simultaneously
- Add document chat history
- Display retrieved document sources
- Display page numbers for retrieved content
- Improve retrieval configuration
- Add configurable chunk sizes and overlap
- Add conversational memory
- Add authentication
- Deploy the application to the cloud
- Add Docker support
- Add evaluation metrics for RAG performance

## Disclaimer

This project is developed for educational and demonstration purposes.

The generated answers are based on retrieved content from the uploaded document and may not always be completely accurate.

## Author

Arun Arumugam

AI/ML Engineer | Python | Machine Learning | Deep Learning | NLP | Generative AI | RAG
