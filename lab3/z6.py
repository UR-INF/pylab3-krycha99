pip.main(["install","numpy"])
import numpy as numpy
def deck():
    karty = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A')
    kolor = ('c','d','h','s')
    deck = list()
    for i in kolor:
        for l in karty:
            deck.append("("+i+","+l+")")
    return deck

def shuffle_deck(deck):
    return numpy.random.permutation(deck)

def deal(deck, n):
    result = list()
    for x in range(n):
        result.append(deck[:5])
    return result

print(deal(shuffle_deck(deck()),2))
