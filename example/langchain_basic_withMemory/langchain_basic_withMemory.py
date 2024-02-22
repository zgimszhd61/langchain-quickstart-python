# 安装langchain和openai库
# !pip install langchain
# !pip install openai

# 导入ConversationBufferMemory类用于对话记忆的管理
from langchain.memory import ConversationBufferMemory
import os

# 设置环境变量OPENAI_API_KEY，用于认证OpenAI API的使用
os.environ["OPENAI_API_KEY"] = "sk-"

# 创建一个对话记忆实例
memory = ConversationBufferMemory()

# 保存两组对话上下文到记忆中
memory.save_context({"input": "hi"}, {"output": "whats up"})
memory.save_context({"input": "who are you"}, {"output": "I`m xiaoming"})

# 加载记忆变量，虽然这里没有明显的使用效果，但通常用于初始化或更新记忆状态
memory.load_memory_variables({})

# 导入OpenAI类和ConversationChain类用于构建对话链
from langchain.llms import OpenAI
from langchain.chains import ConversationChain

# 创建一个OpenAI语言模型实例，设置温度参数为0（产生更确定性的回答）
llm = OpenAI(temperature=0)

# 创建一个对话链实例，传入语言模型和记忆，设置verbose=True以打印详细信息
conversation = ConversationChain(
    llm=llm,
    verbose=True,
    memory=memory
)

# 使用对话链预测输入"hi"的回应
conversation.predict(input="hi")
