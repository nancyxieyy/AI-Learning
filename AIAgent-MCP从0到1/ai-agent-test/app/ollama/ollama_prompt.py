from tkinter.scrolledtext import example
from langchain_core.prompts import ChatPromptTemplate, ChatMessagePromptTemplate, FewShotPromptTemplate, PromptTemplate
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

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

# resp = llm.stream(few_prompt)

chain = few_shot_template | llm
resp =  chain.stream(input={"text": "Thank you!"})

for chunk in resp:
    print(chunk.content, end="")