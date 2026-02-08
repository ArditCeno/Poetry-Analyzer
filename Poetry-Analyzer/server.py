from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from poetry_analyzer import PoetryAI

class Req(BaseModel):
    text:str
    top_k:int=5

app=FastAPI()

app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],allow_headers=["*"])

ai=PoetryAI()
ai.load_poems("poems")

@app.post("/analyze")
def analyze(r:Req):
    return ai.analyze(r.text,r.top_k)

if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=8080)
