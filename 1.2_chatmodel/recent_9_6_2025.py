from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model(model="gemini-2.0-flash", model_provider="google_genai")

result = model.invoke("Hello")

print(result.content)