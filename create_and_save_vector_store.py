VECTOR_STORE_PATH = "path/to/vector_store"  # Define the path where the vector store will be saved
def create_and_save_vector_store(pdf_paths):
    if os.path.exists(VECTOR_STORE_PATH):  # Check if the vector store already exists
    print("Vector store already exists. Delete it if you want to recreate it.")  # Notify the user if the store exists
    return  # Exit the function if the vector store already exists
                    
   print("Creating vector store from PDFs...")  # Notify the user that that vector store creation process is starting
   embeddings = OpenAIEmbeddings()  # Initialize OpenAI embeddings for the documents
   documents = []  # Initialize an empty list to store the documents
                            
   for pdf_path in pdf_paths:  # Iterate through each PDF path in the list
       extracted_pages = extract_text_from_pdf(pdf_path)  # Extract text from the PDF
       for text, page_number, section_title in extracted_pages:  # Iterate through the extracted pages
          chunks = chunk_text(text)  # Split the text into chunks
          docs = [Document(page_content=chunk, metadata={
                    "source": os.path.basename(pdf_path),  # Extract file name from the PDF path
                    "page_number": page_number  # Add page number metadata
          }) for chunk in chunks]  # Create Document objects for each chunk with metadata about the source, page, and section
          documents.extend(docs)  # Add the documents to the documents list
                    
    vector_store = FAISS.from_documents(documents, embeddings)  # Create a vector store from the documents using FAISS
    vector_store.save_local(VECTOR_STORE_PATH)  # Save the vector store to the local path
    print("Vector store saved successfully!")  # Notify the user that the vector store was saved
