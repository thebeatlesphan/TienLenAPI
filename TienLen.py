import random

class TienLen:
	def __init__(self):
		self.none = None
		
	pass

class Card:
	values = { 
		"Two": 12,
		"Three": 0,
		"Four": 1,
		"Five": 2,
		"Six": 3,
		"Seven": 4,
		"Eight": 5,
		"Nine": 6,
		"Ten": 7,
		"Jack": 8,
		"Queen": 9,
		"King": 10,
		"Ace": 11
	}

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
		self.value = Card.values[rank]

	def __str__(self):
		return self.rank + " of " + self.suit

class Deck:
	suits = ["Diamonds", "Hearts", "Spades", "Clubs"]
	ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

	def __init__(self):
		self.deck = []

		for rank in Deck.ranks:
			for suit in Deck.suits:
				self.deck.append(Card(rank, suit))

	def shuffle(self):
		temp = None
		for x in range(len(self.deck)):
			random_position = random.randint(0, 51)
			temp = self.deck[random_position]
			self.deck[random_position] = self.deck[x]
			self.deck[x] = temp

	def deal_card(self):
		return self.deck.pop(0)

class Player():
	def __init__(self):
		self.player1 = []
		self.player2 = []
		self.player3 = []
		self.player4 = []

	def deal_cards(self, new_deck):
		for x in range(12):
			self.player1.append(new_deck.deal_card())
			self.player2.append(new_deck.deal_card())
			self.player3.append(new_deck.deal_card())
			self.player4.append(new_deck.deal_card())
