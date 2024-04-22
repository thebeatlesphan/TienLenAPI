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

    def get_rank(self):
        return self.rank_values[self.rank]

    def get_suit(self):
        return self.suit_rankings[self.suit]

    def __eq__(self, other):
        if isinstance(other, Card):
            return (self.rank == other.rank) and (self.suit == other.suit)
        return False


class Deck:
    # Helper variables
    suits = ["Diamonds", "Hearts", "Spades", "Clubs"]
    ranks = ["Two", "Three", "Four", "Five", "Six", "Seven",
             "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

    # Create a fresh new deck
    def __init__(self):
        self.deck = []
        for rank in Deck.ranks:
            for suit in Deck.suits:
                self.deck.append(Card(rank, suit))

    # Shuffle deck
    def shuffle(self):
        temp = None
        for x in range(len(self.deck)):
            random_position = random.randint(0, 51)
            temp = self.deck[random_position]
            self.deck[random_position] = self.deck[x]
            self.deck[x] = temp

    # Deal card from deck
    def deal_card(self):
        return self.deck.pop(0)


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
    # Intialize game with new deck and players
    def __init__(self):
        self.players = Players()
        self.deck = Deck()
        self.current_player = None
        self.last_hand = None

    # Helper method for sorting
    def compare_ranks(card):
        return card.value

    def compare_suits(card1, card2):
        if card1.rank == card2.rank:
            return Card.suit_rankings[card1.suit] - Card.suit_rankings[card2.suit]
        else:
            return 0

    # Sort low to high by Tien Len standards
    def sort_all_hands(self):
        players = [
            self.players.player1,
            self.players.player2,
            self.players.player3,
            self.players.player4
        ]
        for i in range(len(players)):
            players[i] = sorted(self.players.player1, key=lambda x: (
                Game.compare_ranks(x), cmp_to_key(Game.compare_suits)(x)))

    # Same algorithm
    def sort_one_hand(self, hand):
        result = sorted(hand, key=lambda x: (
            Game.compare_ranks(x), cmp_to_key(Game.compare_suits)(x)))
        return result

    # Find player with 3 of spades to start new game
    def find_three_of_spades(self):
        players = [self.players.player1, self.players.player2,
                   self.players.player3, self.players.player4]
        for i, player in enumerate(players):
            for card in player:
                if card.rank == "Three" and card.suit == "Spades":
                    return i

    # TODO: finish
    def new_current_player(self):
        if self.current_player == 3:
            self.current_player = 0
        else:
            self.current_player += 1

    # Prepare new game
    def new_game(self):
        self.deck.shuffle()
        self.players.deal_cards(self.deck)
        self.sort_all_hands()
        self.current_player = self.find_three_of_spades()

    # GAME LOGIC -----------------------------------------------------
    def get_hand_value(hand):
        value = 0
        for card in hand:
            value += card["value"]
        return value

    def get_suit_value(suit):
        return Card.suit_rankings[suit]

    # Starting with four 2's is an automatic win
    def player_index_has_four_twos(self):
        players = [self.players.player1, self.players.player2,
                   self.players.player3, self.players.player4]
        for index, hand in enumerate(players):
            result = sum(1 for card in hand if card.value == 12)
            if result == 4:
                return index
        return None

    # determine play type : singles, pairs, straights, cows, dbl straights
    # returns False if not valid hand type
    def get_hand_type(self, hand):
        if len(hand) == 1:
            return True, "singles"  # la bai
        elif len(hand) == 2 and hand[0]["value"] == hand[1]["value"]:
            return True, "pairs"  # doi bai
        elif len(hand) == 3 and hand[0]["value"] == hand[1]["value"] and hand[0]["value"] == hand[2]["value"]:
            return True, "triples"
        elif len(hand) == 4 and all(card["value"] == hand[0]["value"] for card in hand):
            return True, "quads"
        # Straights
        elif len(hand) >= 3:
            # check for dbl straights
            for length in range(6, 13, 2):
                if len(hand) == length:
                    if all(hand[i]["value"] == hand[i + 1]["value"] for i in range(0, length, 2)):
                        return True, "double straight"

            # straights
            prev_card = None
            for card in hand:
                # two's cannot be used in normal straights
                if card["value"] == 12:
                    return False, "Cannot play twos"

                if not prev_card:
                    prev_card = card["value"]
                elif card["value"] - 1 == prev_card:
                    prev_card = card["value"]
                else:
                    return False, "Invalid hand type"
            return True, "straight"

        else:
            return False, "Invalid hand type"

    # Check if hand is a 'bomb'
    def is_bomb(self, hand):
        hand_type = self.get_hand_type(hand)
        if hand_type[1] == "quads":
            return True
        elif hand_type[1] == "double straight":
            return True

    # Return highest value card in hand
    def get_highest_value_card(self, hand):
        return hand[-1]

    # Compare suit rankings if values are equal
    def is_higher_suit(self, cardOne, cardTwo) -> bool:
        if cardOne["value"] == cardTwo["value"]:
            return Card.suit_rankings[cardOne["suit"]] > Card.suit_rankings[cardTwo["suit"]]
        else:
            return False, "Cards not same rank"

    def get_number_of_twos(self, hand) -> int:
        result = 0
        for card in hand:
            if card.get_rank() == 12:
                result += 1
        return result

    # Check if play is valid
    def is_valid_play(self, intended_play, last_hand) -> bool:
        # Free board
        if last_hand is None:
            return self.get_hand_type(intended_play)[0]

        # Check for same hand length and type
        if self.get_hand_type(last_hand)[1] == self.get_hand_type(intended_play)[1] and len(last_hand) == len(intended_play):
            # Check for 2s

            last = self.get_highest_value_card(last_hand)
            intended = self.get_highest_value_card(intended_play)
            if last.get_rank() == intended.get_rank():
                return last.get_suit() < intended.get_suit()
            else:
                return last.get_rank() < intended.get_rank()

    