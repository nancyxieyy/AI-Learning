from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, ChatMessagePromptTemplate, FewShotPromptTemplate, PromptTemplate
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

# 1. 初始化模型
llm = ChatOllama(
    disable_streaming=False,
    model="qwen2.5:1.5b"
)

system_message_template = ChatMessagePromptTemplate.from_template(
    template="你是一位{role}专家，擅长回答{domain}领域的问题",
    role="system",
)

human_message_template = ChatMessagePromptTemplate.from_template(
    template="用户问题：{question}",
    role="user",
)

# 2. 定义prompt模版
chat_prompt_template = ChatPromptTemplate.from_messages([
    system_message_template,
    human_message_template
])

# 模版+变量=>提示词
prompt = chat_prompt_template.format_messages(
    role="编程",
    domain="Web开发",
    question="如何构建一个基于Vue的前端应用"
)