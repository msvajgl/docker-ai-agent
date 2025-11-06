from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from .models import ChatMessagePayload, ChatMessage, ChatMessageListItem
from api.db import get_session

router = APIRouter()

@router.get("/")
def chat_health():
    return {"status": "ok"}


@router.get("/recent/", response_model=List[ChatMessageListItem])
def chat_list_messages(session: Session = Depends(get_session)):
   query = select(ChatMessage)
   results = session.exec(query).fetchall()[:10]
   return results

# curl -X POST http://127.0.0.1:8080/api/chats/ -H "Content-Type: application/json" -d '{"message": "hello world"}'

@router.post("/", response_model=ChatMessageListItem)
def chat_create_message(
    payload: ChatMessagePayload,
    session: Session = Depends(get_session)
    ):
    data = payload.model_dump()
    print(data)
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj