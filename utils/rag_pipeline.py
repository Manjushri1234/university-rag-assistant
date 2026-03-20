from utils.web_search import search_web


def run_rag(query, documents, llm):
    relevant_docs = []

    for doc in documents:
        if query.lower() in doc.page_content.lower():
            relevant_docs.append(doc.page_content)

    # If no docs found → use web search
    if not relevant_docs:
        web_data = search_web(query)
        context = web_data
    else:
        context = "\n".join(relevant_docs[:3])

    prompt = f"""
    Use the below context to answer the question.

    Context:
    {context}

    Question:
    {query}
    """

    return llm(prompt)
