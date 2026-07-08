from ddgs import DDGS

def search_web(query):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))

        if not results:
            return "Sorry, I couldn't find any information."

        response = ""

        for i, result in enumerate(results, 1):
            response += f"{i}. {result['title']}\n"
            response += f"{result['body']}\n"
            response += f"{result['href']}\n\n"

        return response

    except Exception as e:
        return f"Internet Search Error:\n{e}"