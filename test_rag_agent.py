import os
import sys
import unittest
from unittest.mock import patch, MagicMock

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from rag_agent import RagAgent
import config

class TestRagAgent(unittest.TestCase):
    
    @patch('rag_agent.OpenAIEmbeddings')
    @patch('rag_agent.ChatOpenAI')
    @patch('rag_agent.Chroma')
    def setUp(self, mock_chroma, mock_chat_openai, mock_embeddings):
        # Mock the OpenAI API key
        os.environ["OPENAI_API_KEY"] = "test_api_key"
        
        # Create a mock for the embeddings
        self.mock_embeddings_instance = MagicMock()
        mock_embeddings.return_value = self.mock_embeddings_instance
        
        # Create a mock for the LLM
        self.mock_llm_instance = MagicMock()
        mock_chat_openai.return_value = self.mock_llm_instance
        
        # Create a mock for the vectorstore
        self.mock_vectorstore = MagicMock()
        mock_chroma.return_value = self.mock_vectorstore
        
        # Initialize the RAG agent
        self.rag_agent = RagAgent()
    
    def test_initialization(self):
        """Test that the RAG agent initializes correctly."""
        self.assertIsNotNone(self.rag_agent)
        self.assertIsNotNone(self.rag_agent.embeddings)
        self.assertIsNotNone(self.rag_agent.llm)
        self.assertIsNotNone(self.rag_agent.text_splitter)
    
    @patch('os.path.exists')
    @patch('glob.glob')
    @patch('rag_agent.process_knowledge_document')
    def test_load_knowledge_base(self, mock_process_doc, mock_glob, mock_exists):
        """Test loading the knowledge base."""
        # Mock the existence of the knowledge base directory
        mock_exists.return_value = True
        
        # Mock finding document files
        mock_glob.return_value = ["knowledge_base/test_doc.txt"]
        
        # Mock processing a document
        mock_process_doc.return_value = {
            "text": "This is a test document.",
            "topic": "test"
        }
        
        # Mock the text splitter
        self.rag_agent.text_splitter.split_text = MagicMock(return_value=["This is a test chunk."])
        
        # Mock the vectorstore
        self.rag_agent.vectorstore = MagicMock()
        
        # Call the method
        self.rag_agent.load_knowledge_base()
        
        # Assert that the document was processed
        mock_process_doc.assert_called_once_with("knowledge_base/test_doc.txt")
        
        # Assert that the text was split
        self.rag_agent.text_splitter.split_text.assert_called_once_with("This is a test document.")
        
        # Assert that documents were added to the vectorstore
        self.rag_agent.vectorstore.add_documents.assert_called_once()
    
    def test_solve_question(self):
        """Test solving a question."""
        # Mock the vectorstore retriever
        mock_retriever = MagicMock()
        mock_doc = MagicMock()
        mock_doc.page_content = "Test content"
        mock_retriever.get_relevant_documents.return_value = [mock_doc]
        self.rag_agent.vectorstore = MagicMock()
        self.rag_agent.vectorstore.as_retriever.return_value = mock_retriever
        
        # Mock the QA chain
        mock_qa_chain = MagicMock()
        mock_qa_chain.invoke.return_value = {"result": "Test solution"}
        
        # Patch the RetrievalQA.from_chain_type method
        with patch('rag_agent.RetrievalQA.from_chain_type', return_value=mock_qa_chain):
            # Call the method
            result = self.rag_agent.solve_question("What is the derivative of x^2?")
            
            # Assert that the result is correct
            self.assertEqual(result["solution"], "Test solution")
            self.assertFalse(result["error"])

if __name__ == "__main__":
    unittest.main()