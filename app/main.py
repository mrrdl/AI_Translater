from fastapi import FastAPI,BackgroundTasks,HTTPException,Request,Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from fastapi.templating import Jinja2Templates
from schemas import TranslationRequest,TaskResponse
from crud import create_translation_task
from database import get_db,engine
import models

models.Base.metadata.create_all(blind=engine)

app=FastAPI()
templates=Jinja2Templates(directory='templates')

@app.get('/index',response_class=HTMLResponse)
def index(request:Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post('/translate',response_model=schemas.TaskResponse)
def translation(request:schemas.TranslationRequest):
    task=crud.create_translation_task(get_db.db,request.text,request.languages,)

    BackgroundTasks.add_task(perform_translation)

    return {"task_id":{task_id}}