from branch import Branch
from issue import Issue
from pydantic import BaseModel
from typing import List

class Repository(BaseModel):
    repo_id: str
    branches: List[Branch]
    tags: List[str]
    issues: List[Issue]

