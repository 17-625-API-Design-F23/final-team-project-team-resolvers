from commit import Commit
from pydantic import BaseModel
from typing import List

class Branch(BaseModel):
    branch_id: str
    commits: List[Commit]