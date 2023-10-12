import random


class Card:
    """  class to describe cards in a pack """
    def __init__(self, number):
        self._card_number = number

    def get_suit(self):
        suit_number= self._card_number //13
        if suit_number == 0:
            return "S"
        if suit_number == 1:
            return "H"
        if suit_number == 2:
            return "D"
        if suit_number == 3:
            return "C"
        """ return a string 'C', 'S', 'H', 'D' """
        pass

    def get_value(self):
        value = self._card_number%13
        cards_value=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        """ return a string 'A'..'10', 'J', 'Q', 'K' """
        return cards_value[value]
        pass

    def get_short_name(self):
        return(f"{self.get_value}{self.get_suit}")
        pass

    def get_long_name(self):
        """ return card name eg 'Ten of Diamonds' """
        suits = {
            "S": "Spades",
            "H": "Hearts",
            "D": "Diamonds",
            "C": "Clubs"
        }
        values = {
            "A": "Ace",
            "2": "Two",
            "3": "Three",
            "4": "Four",
            "5": "Five",
            "6": "Six",
            "7": "Seven",
            "8": "Eight",
            "9": "Nine",
            "10": "Ten",
            "J": "Jack",
            "Q": "Queen",
            "K": "King"
        }
        return f"{values[self.get_value()]} of {suits[self.get_suit()]}"


class Deck:
    """ A class to contain a pack of cards with methods for shuffling, adding or removing cards etc. """
    def __init__(self):
        self._card_list = []
        for i in range(52):
            self._card_list.append(Card(i))

    def length(self):
        print(len(self._card_list))
        pass

    def shuffle_deck(self):
        """ shuffles the cards """
        random.shuffle(self._card_list)

    def take_top_card(self):
        """ removes the top card from the deck and returns it (as a card object) """
        print(self._card_list[1])
        pass


card = Card(52)
print(card.get_suit()) 
deck = Deck()
deck.shuffle_deck()
for i in range(52):
    card = deck.take_top_card()
    print(Card.get_long_name())

    