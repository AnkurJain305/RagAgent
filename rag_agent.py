import os
import glob
from typing import List, Dict, Any, Optional

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.schema.document import Document

import config
from utils.document_processing import process_knowledge_document
from utils.text_processing import clean_text, format_solution, parse_question
from utils.math_utils import solve_equation, differentiate, integrate, plot_function

class RagAgent:
    def __init__(self):
        """Initialize the RAG agent with necessary components."""
        # Check if API key is available
        if not config.OPENAI_API_KEY:
            raise ValueError("OpenAI API key is not set. Please set it in the .env file.")
        
        # Initialize embeddings
        self.embeddings = OpenAIEmbeddings(
            model=config.EMBEDDING_MODEL,
            openai_api_key=config.OPENAI_API_KEY
        )
        
        # Initialize LLM
        self.llm = ChatOpenAI(
            model_name=config.MODEL_NAME,
            temperature=0.2,
            openai_api_key=config.OPENAI_API_KEY
        )
        
        # Initialize text splitter for chunking documents
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.CHUNK_SIZE,
            chunk_overlap=config.CHUNK_OVERLAP
        )
        
        # Initialize vector store if it exists
        self.vectorstore = None
        if os.path.exists(config.CHROMA_PERSIST_DIRECTORY):
            self.vectorstore = Chroma(
                persist_directory=config.CHROMA_PERSIST_DIRECTORY,
                embedding_function=self.embeddings
            )
        
        # Initialize prompt template
        self.prompt_template = PromptTemplate(
            template=config.QUESTION_PROMPT_TEMPLATE,
            input_variables=["question", "context"]
        )
    
    def load_knowledge_base(self, knowledge_dir: str = "knowledge_base") -> None:
        """Load documents from the knowledge base directory."""
        # Create knowledge directory if it doesn't exist
        if not os.path.exists(knowledge_dir):
            os.makedirs(knowledge_dir)
            print(f"Created knowledge base directory: {knowledge_dir}")
            return
        
        # Get all document files
        document_paths = []
        for ext in [".pdf", ".docx", ".txt"]:
            document_paths.extend(glob.glob(os.path.join(knowledge_dir, f"**/*{ext}"), recursive=True))
        
        if not document_paths:
            print("No documents found in the knowledge base directory.")
            return
        
        # Process documents
        documents = []
        for doc_path in document_paths:
            doc_info = process_knowledge_document(doc_path)
            if doc_info["text"]:
                # Create document chunks
                chunks = self.text_splitter.split_text(doc_info["text"])
                for i, chunk in enumerate(chunks):
                    metadata = {
                        "source": doc_path,
                        "chunk": i,
                        "topic": doc_info["topic"] or "general"
                    }
                    documents.append(Document(page_content=chunk, metadata=metadata))
        
        # Create or update vector store
        if not documents:
            print("No valid document content found.")
            return
        
        if self.vectorstore is None:
            self.vectorstore = Chroma.from_documents(
                documents=documents,
                embedding=self.embeddings,
                persist_directory=config.CHROMA_PERSIST_DIRECTORY
            )
            self.vectorstore.persist()
        else:
            # Add documents to existing vectorstore
            self.vectorstore.add_documents(documents)
            self.vectorstore.persist()
        
        print(f"Loaded {len(documents)} document chunks into the knowledge base.")
    
    def solve_question(self, question: str) -> Dict[str, Any]:
        """Solve a JEE mathematics question using the RAG approach."""
        # Parse the question
        parsed_question = parse_question(question)
        clean_question = parsed_question["question"]
        
        # Check if vectorstore is initialized
        if self.vectorstore is None:
            return {
                "solution": "Knowledge base not initialized. Please load the knowledge base first.",
                "error": True
            }
        
        # Retrieve relevant context from the knowledge base
        retriever = self.vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": config.TOP_K_RETRIEVAL}
        )
        
        # Filter by topic if available
        search_kwargs = {}
        if parsed_question["topic"]:
            search_kwargs["filter"] = {"topic": parsed_question["topic"]}
        
        # Get relevant documents
        docs = retriever.get_relevant_documents(clean_question)
        context = "\n\n".join([doc.page_content for doc in docs])
        
        # Create QA chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            chain_type_kwargs={"prompt": self.prompt_template}
        )
        
        # Generate solution
        try:
            result = qa_chain.invoke({"query": clean_question})
            solution_text = result["result"]
            
            # Format the solution
            formatted_solution = format_solution(solution_text)
            
            # Check if we need to generate any plots
            plots = []
            # Look for function plotting requests in the question
            if "graph" in question.lower() or "plot" in question.lower():
                for expr in parsed_question["math_expressions"]:
                    if "=" in expr and not "==" in expr:
                        # This might be a function definition
                        parts = expr.split("=")
                        if len(parts) == 2 and "(" in parts[0] and ")" in parts[0]:
                            # Extract the variable and expression
                            var_match = re.search(r'(\w)\(\w\)', parts[0])
                            if var_match:
                                var = var_match.group(1)
                                plot_img = plot_function(parts[1], variable=var)
                                if plot_img:
                                    plots.append(plot_img)
            
            return {
                "solution": formatted_solution,
                "plots": plots,
                "error": False
            }
            
        except Exception as e:
            return {
                "solution": f"Error solving the question: {str(e)}",
                "error": True
            }
    
    def add_document(self, file_path: str) -> bool:
        """Add a single document to the knowledge base."""
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return False
        
        doc_info = process_knowledge_document(file_path)
        if not doc_info["text"]:
            print(f"No text content found in {file_path}")
            return False
        
        # Create document chunks
        chunks = self.text_splitter.split_text(doc_info["text"])
        documents = []
        for i, chunk in enumerate(chunks):
            metadata = {
                "source": file_path,
                "chunk": i,
                "topic": doc_info["topic"] or "general"
            }
            documents.append(Document(page_content=chunk, metadata=metadata))
        
        # Add to vector store
        if self.vectorstore is None:
            self.vectorstore = Chroma.from_documents(
                documents=documents,
                embedding=self.embeddings,
                persist_directory=config.CHROMA_PERSIST_DIRECTORY
            )
        else:
            self.vectorstore.add_documents(documents)
        
        self.vectorstore.persist()
        print(f"Added {len(documents)} chunks from {file_path} to the knowledge base.")
        return True