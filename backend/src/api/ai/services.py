from api.ai.llm import get_openai_llm
from api.ai.schemas import EmailMessageSchema

def generate_email_message(query:str) -> EmailMessageSchema:
    llm_base = get_openai_llm()
    llm = llm_base.with_structured_output(EmailMessageSchema)

    messages = [
        ("system",
        "You are a helpfull assistant for research and composing plaintext emails. Do not use markdown in you response"),
        ("human",
        f"{query}. Do not use markdown in your response on plaintext")
    ]

    return llm.invoke(messages)