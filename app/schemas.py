from pydantic import BaseModel
from typing import List,Dict

class TranslationRequest(BaseModel):
    text:str
    lang:List[str]

class TaskResponse(BaseModel):
    task_id: str

class TransStatus(BaseModel):
    task_id: str
    status: str
    translations:Dict[str,str]