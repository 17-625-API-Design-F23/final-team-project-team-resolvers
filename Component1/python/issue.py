from comment import Comment
from pydantic import BaseModel
from typing import List

class Issue(BaseModel):
    issue_id: str
    user_id: str
    status: str
    description: str
    date: str
    comments: List[Comment]