from pydantic import BaseModel
from typing import List, Dict

class Commit(BaseModel):
    commit_hash: str
    tags: List[str]
    user_id: str
    dir: Dict[str, List[str]]