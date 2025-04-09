# do with OpenAI (does not work with google)
# there is no guarantee that llm will not do mistake, here no data validation is there

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# schema
class Review(TypedDict):
    summary: Annotated[str, "Short summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "What is the sentiment of this review? Positive(pos) or Negative(neg)"]
    pros: Annotated[Optional[list[str]], "mention pros only if discussed in review"]
    cons: Annotated[Optional[list[str]], "mention cons only if discussed in review"]


structured_model = model.with_structured_output(Review)

result = structured_model.invoke("The hardware is great but software feels bloated")

print(result)
print(result["summary"])
print(result["sentiment"])
