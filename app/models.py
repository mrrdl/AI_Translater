from sqlalchemy import Column,Integer,String,Text,Json
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class TranslationTask(Base):
    __tablename__ = 'translation_task'
    id=Column(Integer,primary_key=True,index=True)
    text=Column(Text,nullable=False)
    languages=Column(Json,nullable=False)
    status=Column(String,"in progress")

    translation=Column(Json,default={})
