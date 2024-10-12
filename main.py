from fastapi import FastAPI
from extract_frames import extract

app = FastAPI()

@app.post("/extract_endpoint")
def extract_api(input_param: str):
    result = extract(input_param)
    return {"result": result}

@app.get("/hello")
def hello():
    return "hello world"
