import collections
from random import choice

OtherCard = collections.namedtuple('OtherCard', ['rank', 'suit'])

class Card:
    """
    This defines a card in our application
    """
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        return str(self)

class FrenchDeck:
    """
    This defines a french deck of cards 
    in our python application
    """
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()
    
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        
    def __getitem__(self, position):
        return self.cards[position]
    
    def __len__(self):
        return len(self.cards)
    
    def __str__(self):
        text = [f"* {card} \n" for card in self.cards]
        text = "".join(text)
        return f"{len(self.cards)} cards" + text
    
    
if __name__ == "__main__":
    my_deck = FrenchDeck()
    print(my_deck)
    print("The size of the deck is:", len(my_deck))
    print("The first card is:", my_deck[0])
    print("A random card is : ", choice(my_deck))
    print("The upper deck : ", my_deck[:3])
    print("The lower deck : ", my_deck[-3:])
    
    for card in my_deck:
        print(card)

        