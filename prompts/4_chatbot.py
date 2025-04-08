from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

history = []

while True:
    user = input("User: ")
    history.append("User: "+user)

    if user == "exit":
        break

    ai = model.invoke(history)
    print("AI: ", ai.content)
    history.append("AI: "+ai.content)