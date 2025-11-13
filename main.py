from fastapi import FastAPI
import uvicorn
import pydantic
import fence
import caeser

app = FastAPI()

@app.get("/test")
def get_test():
    return {"msg": "hi from test"}

@app.get("/test/{name}")
def get_name(name):
    with open("names.txt","a") as f:
        f.write(name)
    return {"msg": "saved user"}

@app.post("/caesar")
def post_caesar(text:dict):
    letter = text["encrypted_text"]
    return caeser.encrypted_caeser(letter)

@app.get("/fence/encrypt")
def get_encrypt_fance(text:str):
    return fence.encrypt_fance(text)

if __name__ == "__main__":
    uvicorn.run(app, host = "localhost", port = 8000)