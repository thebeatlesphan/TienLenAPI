import TienLen

class Bot:
    def __init__(self, hand):
        self.hand = []
        self.combination_cards = []
        self.single_cards = []
        for card in hand:
            self.hand.append(TienLen.Card(card['rank'], card['suit']))

    def dead_Cards(self):
        
        pass

    def index_of_straights(self):
        try:
            indices = set()
            for index, card in enumerate(self.hand):
                if card['value']+1 == self.hand[index+1]['value'] and self.hand[index+1]['value']+1 == self.hand[index+2]['value']:
                    indices.add(index)
                    indices.add(index+1)
                    indices.add(index+2)
        except IndexError:
            pass
        finally:
            return indices 

    def index_of_pairs(self):
        try:
            indices = set()
            for index, card in enumerate(self.hand):
                if card['value'] == self.hand[index+1]['value']:
                    indices.add(index)
                    indices.add(index+1)
        except IndexError:
            pass
        finally:
            return indices

    def play_singles(self, last_play):
        pass

test = [{"rank":"Five","suit":"Spades","value":2},{"rank":"Five","suit":"Diamonds","value":2},{"rank":"Six","suit":"Spades","value":3},{"rank":"Six","suit":"Diamonds","value":3},{"rank":"Seven","suit":"Clubs","value":4},{"rank":"Seven","suit":"Diamonds","value":4},{"rank":"Eight","suit":"Hearts","value":5},{"rank":"Nine","suit":"Spades","value":6},{"rank":"Jack","suit":"Hearts","value":8},{"rank":"Queen","suit":"Spades","value":9},{"rank":"King","suit":"Spades","value":10},{"rank":"King","suit":"Hearts","value":10},{"rank":"Ace","suit":"Spades","value":11}]
#for i,x in enumerate(test):
    #print(x['value'])
#print(test[1]['value'])
print(Bot(test).index_of_straights())
print(Bot(test).index_of_pairs())
print("hello world")
