from fastapi import FastAPI
import deta

app = FastAPI()

log = deta.Base("log")

@app.get("/")
def index():
    return {"message": "Hi, I exist!"} 