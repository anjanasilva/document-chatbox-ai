def ask_question(request: QueryRequest):
    vector_store = load_vector_store() # Loading the vector store
    docs = vector_store.similarity_search(request.question, k=3)  # Perform similarity search to find the top 3 matching documents
    if not docs:  # Check if no documents were found
            return {"answer": "Cannot find answers using the document.", "sources": []}  # Return a message if no relevant documents were found

    context = "\n\n".join([doc.page_content for doc in docs])  # Combine the page contents of the top documents into a single context
    sources = list(set(f"{doc.metadata['source']} (Page {doc.metadata['page_number']})" for doc in docs))  # Get the unique sources and page numbers for the documents

    from langchain_openai import ChatOpenAI  # Import the ChatOpenAI class for interaction with GPT-4
    llm = ChatOpenAI(model="gpt-4", temperature=0)  # Initialize the GPT-4 model with temperature set to 0 for deterministic responses

    prompt = f"Using only the following document excerpts, answer the question:\n\n{context}\n\nQuestion: {request.question}"  # Construct the prompt for the language model with the context and the question
    answer = llm.invoke(prompt)  # Get the answer from GPT-4 based on the provided context

    return {"answer": answer, "sources": sources}  # Return the answer along with the sources from the documents
