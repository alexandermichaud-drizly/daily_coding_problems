from collections import namedtuple
from random import randint

Card = namedtuple('Card', ['val','suit'])

SUITS = [
		'Diamonds',
		'Clubs',
		'Spades',
		'Hearts'
]

VALUES = [
		'Ace',
		'Two',
		'Three',
		'Four',
		'Five',
		'Six',
		'Seven',
		'Eight',
		'Nine',
		'Ten',
		'Jack',
		'Queen',
		'King'
]

class Deck:
		def __init__(self):
				self.cards = []
				for suit in SUITS:
						for val in VALUES:
								card = Card(val, suit)
								self.cards.append(card)

		def shuffle(self, k):
				l = k * 52
				for i in range(52):
						dest = ( randint(0,l) + randint(0,l) ) % 52  
						self.__swap(i,dest)

		def __swap(self, i, j):
				swap = self.cards[i]
				self.cards[i] = self.cards[j]
				self.cards[j] = swap

deck = Deck()
deck.shuffle(8)

for card in deck.cards:
		print(card.val + " of " + card.suit)

