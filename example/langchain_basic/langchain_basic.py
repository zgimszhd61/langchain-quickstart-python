# 安装 langchain 和 openai 库。这些库提供了调用 OpenAI API 和构建聊天模型的功能。
# !pip install langchain
# !pip install openai

# 导入所需的模块。这些模块用于创建聊天模型、定义提示模板和解析模型输出。
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

# 设置 OpenAI API 密钥。这个密钥是访问 OpenAI 服务所必需的。
os.environ["OPENAI_API_KEY"] = "sk-"

# 定义一个聊天提示模板。这里定义的模板是“告诉我一个关于 {topic} 的短笑话”，其中 {topic} 是一个动态插入的主题。
prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")

# 创建一个聊天模型的实例。这里使用的是 OpenAI 提供的聊天模型。
model = ChatOpenAI()

# 创建一个输出解析器的实例。这个解析器用于将模型的输出转换为字符串格式。
output_parser = StrOutputParser()

# 将提示模板、模型和输出解析器连接起来，形成一个处理链。这个处理链用于执行从生成提示到获取模型输出的整个流程。
chain = prompt | model | output_parser

# 调用处理链，并传入一个主题（这里的示例主题是“ice cream”），以生成关于该主题的短笑话。
chain.invoke({"topic": "ice cream"})
