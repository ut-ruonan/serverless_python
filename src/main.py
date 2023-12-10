from fastapi import FastAPI
from src.env import config

MODE=config("MODE", cast=str, default="testing")
app = FastAPI()

@app.get("/")
def home_page():
    return {"Hello": "World", "MODE": MODE}

# @app.post("/")
# def home_handle_data_page():
#     return {"Hello": "World"}