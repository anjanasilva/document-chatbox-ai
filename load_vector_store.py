def load_vector_store():
   if not os.path.exists(VECTOR_STORE_PATH):  # Check if the vector store exists
      raise FileNotFoundError("Vector store not found! Run `create_and_save_vector_store()` first.")  # Raise an error if the vector store is not found
   print("Loading existing vector store...")  # Notify the user that the vector store is being loaded
   return FAISS.load_local(VECTOR_STORE_PATH, OpenAIEmbeddings(), allow_dangerous_deserialization=True)  # Load the vector store from the local path with embeddings                  
