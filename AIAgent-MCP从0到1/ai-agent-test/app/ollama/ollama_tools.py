from tkinter.scrolledtext import example

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, ChatMessagePromptTemplate, FewShotPromptTemplate, PromptTemplate
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

# 1. 初始化模型
llm = ChatOllama(
    disable_streaming=False,
    model="deepseek-r1:1.5b"
)

# 3.
system_message_template = ChatMessagePromptTemplate.from_template(
    template="你是一位{role}专家，擅长回答{domain}领域的问题",
    role="system",
)

human_message_template = ChatMessagePromptTemplate.from_template(
    template="用户问题：{question}",
    role="user",
)

# 2. 定义prompt模版
prompt_template = ChatPromptTemplate.from_messages([
    system_message_template,
    human_message_template
])

prompt = prompt_template.format_messages(
    role="编程",
    domain="Web开发",
    question="如何构建一个基于Vue的前端应用"
)

#

example_prompt = "输入：{input}\n输出：{output}"
examples = [
    {"input": "将'Hello'翻译成中文", "output": "你好"},
    {"input": "将'Goodbye'翻译成中文", "output": "再见"}
]

few_shot_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=PromptTemplate.from_template(example_prompt),
    prefix="请将以下英文翻译成中文：",
    suffix="输入：{text}\n输出：",
    input_variables=["text"],
)

# print(few_shot_template)
few_prompt = few_shot_template.format(text="Thank you!")
print(few_prompt)

resp = llm.stream(few_prompt)

for chunk in resp:
    print(chunk.content, end="")