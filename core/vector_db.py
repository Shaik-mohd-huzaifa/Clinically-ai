from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_upstage import UpstageEmbeddings, ChatUpstage
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv() 


os.environ["UPSTAGE_API_KEY"] = os.getenv("UPSTAGE_API_KEY")

# Initialize embeddings
embeddings = UpstageEmbeddings(
  api_key="up_bXD0hpW4zsRXlkA9e5LxayEcgwabg",
  model="solar-embedding-1-large"
)

# Initialize OpenAI client
client = ChatUpstage()


def VectorStore(filename):
    # Load the text file
    loader = TextLoader("./core/output.txt")
    documents = loader.load()

    # Split the documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=30, separator='\n')
    docs = text_splitter.split_documents(documents=documents)
    
    # Create a FAISS vectorstore from the documents
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("./Patient_Reports/" + filename)
    
    # Define the prompt template manually
    template = """You are an HealthCare Assistant. Who summarizes patient reports for the doctors:

    Context:
    {context}

    Question:
    {question}

    Answer:"""

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=template
    )
    
    # Create the Retrieval QA chain
    retrieval_chain = RetrievalQA.from_chain_type(
        llm=client,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={"prompt": prompt}
    )
    
    # Run the retrieval chain with a query
    res = retrieval_chain.invoke({"query": "Summarize the report"})
    return res
