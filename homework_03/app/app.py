from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/ping/")
def get_ping():
    return {"message": "pong"}