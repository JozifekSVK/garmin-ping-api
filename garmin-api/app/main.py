# main.py
from fastapi import FastAPI
from fastapi import FastAPI

app = FastAPI()

@app.post("/post-req/")
async def create_user(request_data: dict) -> dict:

    print(request_data)
    return {
        "msg": "we got data succesfully"
    }

@app.get("/")
async def read_root():
    return {"Hello": "this is garming connect api"}
