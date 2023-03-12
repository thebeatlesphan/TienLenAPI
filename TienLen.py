import random
from functools import cmp_to_key

class Card:
	rank_values = { 
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

	suit_rankings = {
		"Spades": 0,
		"Clubs": 1,
		"Diamonds": 2,
		"Hearts": 3
	}

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
		self.value = Card.rank_values[rank]

	def __str__(self):
		return f"{self.rank} of {self.suit}"

	def __getitem__(self, key):
		return self.__dict__[key]

	def get_suit(self):
		return self.rank_values[self.rank]
	
	def get_suit(self):
		return self.suit_rankings[self.suit]
	
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

	def sort_cards(self):
		pass
	
class Players:
	def __init__(self):
		self.player1 = []
		self.player2 = []
		self.player3 = []
		self.player4 = []

	def __str__(self):
		return f"Player1 has {len(self.player1)} cards\nPlayer2 has {len(self.player2)} cards\nPlayer3 has {len(self.player3)} cards\nPlayer4 has {len(self.player4)} cards"
	
	def deal_cards(self, new_deck):
		for x in range(13):
			self.player1.append(new_deck.deal_card())
			self.player2.append(new_deck.deal_card())
			self.player3.append(new_deck.deal_card())
			self.player4.append(new_deck.deal_card())

class Game:
	def __init__(self):
		self.players = Players()
		self.deck = Deck()
		self.current_player = None
		self.last_hand = None

	def compare_ranks(card):
		return card.value
	
	def compare_suits(card1, card2):
		if card1.rank == card2.rank:
			return Card.suit_rankings[card1.suit] - Card.suit_rankings[card2.suit]
		else:
			return 0

	def sort_all_hands(self):
		self.players.player1 = sorted(self.players.player1, key=lambda x: (Game.compare_ranks(x), cmp_to_key(Game.compare_suits)(x)))
		self.players.player2 = sorted(self.players.player2, key=lambda x: (Game.compare_ranks(x), cmp_to_key(Game.compare_suits)(x)))
		self.players.player3 = sorted(self.players.player3, key=lambda x: (Game.compare_ranks(x), cmp_to_key(Game.compare_suits)(x)))
		self.players.player4 = sorted(self.players.player4, key=lambda x: (Game.compare_ranks(x), cmp_to_key(Game.compare_suits)(x)))
		
	def sort_one_hand(self, hand):
		result = sorted(hand, key=lambda x: (Game.compare_ranks(x), cmp_to_key(Game.compare_suits)(x)))
		return result
	
	def find_three_of_spades(self):
		players = [self.players.player1, self.players.player2, self.players.player3, self.players.player4]
		for i, player in enumerate(players):
			for card in player:
				if card.rank == "Three" and card.suit == "Spades":
					return i

	def new_current_player(self):
		if self.current_player == 3:
			self.current_player = 0
		else:
			self.current_player += 1

	def new_game(self):
		self.deck.shuffle()
		self.players.deal_cards(self.deck)
		self.sort_all_hands()
		self.current_player = self.find_three_of_spades()
	
	# GAME LOGIC
	def hand_value(hand):
		value = 0
		for card in hand:
			value += card["value"]
		return value

	def suit_value(suit):
		return Card.suit_rankings[suit]
	
	def can_play_intended_hand(intended_play, last_play) -> bool:
		if len(intended_play) != len(last_play): # need to rethink bo
			return False
		
		# First play of the game
		if last_play == None: 
			return False
		
		# Singles
		elif len(last_play) == 1:
			if len(intended_play) != 1:
				print("if statement")
				return False
			else:
				print("else statement")
				return Game.singles(intended_play, last_play)
	
	# Starting with four 2's is an automatic win
	def player_index_has_four_twos(self):
		players = [self.players.player1, self.players.player2, self.players.player3, self.players.player4]
		for index, hand in enumerate(players):
				result = sum(1 for card in hand if card.value == 12)
				if result == 4:
					return index
		return None

	def singles(intended_play, last_play):
		_intended = Game.hand_value(intended_play)
		_last = Game.hand_value(last_play)
		if _intended == _last:
			return Game.suit_value(intended_play.suit) > Game.suit_value(last_play.suit)
		else:
			return _intended > _last

