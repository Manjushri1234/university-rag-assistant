def run_rag(query, vectorstore, llm):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    docs = retriever.get_relevant_documents(query)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Answer the question based on the context below.

    Context:
    {context}

    Question:
    {query}
    """

    response = llm.invoke(prompt)

    return response.content
