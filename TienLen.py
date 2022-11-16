class TienLen:
	pass

class Card:
	values = { 
		"Two": 2,
		"Three": 3,
		"Four": 4,
		"Five": 5,
		"Six": 6,
		"Seven": 7,
		"Eight": 8,
		"Nine": 9,
		"Ten": 10,
		"Jack": 10,
		"Queen": 10,
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
		
deck = Deck()
print(deck.deck[0])