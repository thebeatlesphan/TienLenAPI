# NAME: TienLenAPI
# AUTHOR: Andy Phan
# DESCRIPTION: API for a card game

import logging
from Bot import Bot
from TienLen import Game
from fastapi import FastAPI, Request
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

class Hand(BaseModel):
	hand: list

class HandsToEvaluate(BaseModel):
	intended_play: list
	last_play: Optional[list] = None

class PlayBot(BaseModel):
	bot_hand: list
	last_play: Optional[list] = None

@app.get("/")
def read_root():
	return {"hello": "world"}

# req: null
# res: 4 player game of Tien Len (3 bots)
@app.get("/new-game")
def new_game():
	game = Game()
	game.new_game()
	return game

# req: [intended_play, last_play]
# res: true / false if intended_play is valid
@app.post("/submit-play")
async def submit_play(item: HandsToEvaluate):
	_item = item.dict()
	_intended = _item["intended_play"]
	_last = _item["last_play"]

	game = Game()
	check = game.check_valid_intended_play(_intended, _last)
	print(check)
	return {check}

# req: [bot_hand, last_play]
# res: [bot_hand, bot_play]
@app.post("/bot")
async def bot(item: PlayBot):
	_bot = Bot(item.bot_hand)
	return {"item": _bot}

# test
@app.post("/check")
async def check(item: Hand):
	_item = item.dict()
	_item = _item["hand"]

	check = Game.determine_play_type(_item)
	return {check}
