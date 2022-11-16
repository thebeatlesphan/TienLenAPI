# NAME: TienLenAPI
# AUTHOR: Andy Phan
# DESCRIPTION: API for a card game

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
	return {"hello": "world"}