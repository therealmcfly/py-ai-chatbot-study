from dotenv import load_dotenv
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

chat_history = []

system_message = "You are a AI chatbot."
chat_history.append(system_message)

# Chat loop
while True:
    query = input("You: ")
    if query == "exit":
        break
    chat_history.append(HumanMessage(content=query))

    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))

    print("AI: ", response)

print("---- Message History ----")
print(chat_history)
