# NAME: TienLenAPI
# AUTHOR: Andy Phan
# DESCRIPTION: API for a card game

import TienLen

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# copy and pasted from : works like a charm for CORS origin blocked
# https://stackoverflow.com/questions/65635346/how-can-i-enable-cors-in-fastapi

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
	return {"hello": "world"}

@app.get("/deal-cards")
def create_deck():
	deck = TienLen.Deck()
	deck.shuffle()
	players = TienLen.Player()
	players.deal_cards(deck)
	return players

# Create AI
# AI needs bot_hand and last_played_hand to determine best play
# best play = 