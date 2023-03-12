# NAME: TienLenAPI
# AUTHOR: Andy Phan
# DESCRIPTION: API for a card game

import logging
from Bot import Bot
from TienLen import Game
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Any

# copy and pasted from : works like a charm for CORS origin blocked
# https://stackoverflow.com/questions/65635346/how-can-i-enable-cors-in-fastapi

app = FastAPI()

origins = ["*", "127.0.0.1:5500"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class HandsToEvaluate(BaseModel):
	intended_play: list
	last_play: Optional[list] = None

class PlayBot(BaseModel):
	bot_hand: list
	last_play: Optional[list] = None

@app.get("/")
def read_root():
	return {"hello": "world"}

@app.get("/new-game")
def new_game():
	game = Game()
	game.new_game()
	return game

@app.post("/submit-play")
async def submit_play(item: HandsToEvaluate):
	print(item)
	return {'item': item}

@app.post("/bot")
async def bot(item: PlayBot):
	_bot = Bot(item.bot_hand)
	return {"item": _bot}