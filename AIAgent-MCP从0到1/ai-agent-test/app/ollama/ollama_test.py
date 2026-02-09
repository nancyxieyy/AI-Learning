from langchain_ollama import ChatOllama

"""
使用 Ollama 来调用模型
"""
if __name__ == '__main__':
    llm = ChatOllama(
        model="deepseek-r1:1.5b",
    )

    messages = [
        (
            "system",
            "You are a helpful assistant that translates English to French. Translate the user sentence.",
        ),
        ("human", "I love programming."),
    ]
    ai_msg = llm.stream(messages)

    for chunk in ai_msg:
        print(chunk.content, end="")