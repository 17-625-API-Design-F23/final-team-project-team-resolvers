from pydantic import BaseModel

class Comment(BaseModel):
    user_id: str
    date: str
    content: str