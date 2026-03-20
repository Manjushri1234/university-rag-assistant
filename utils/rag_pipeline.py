def run_rag(query, documents, llm):
    # Simple keyword-based retrieval
    relevant_docs = []

    for doc in documents:
        if query.lower() in doc.page_content.lower():
            relevant_docs.append(doc.page_content)

    context = "\n".join(relevant_docs[:3])  # top 3 matches

    prompt = f"""
    Use the below context to answer the question.

    Context:
    {context}

    Question:
    {query}
    """

    return llm(prompt)
