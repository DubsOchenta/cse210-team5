
# Card Class
# CSE210 By Robert Odell

import random


class Card:
    """A card drawn from a deck with a different value and suit name.

    The purpose of Card is to generate a random card value
    and suit name and return the point value for that card.

     Attributes:
        suits (dict[int, str]): A dictionary with an int as the suit value
        for the dict key and a string as the suit name for the dict value.

        values (dict[int, str]): A dictionary with an int as the card value
        for the dict key and a string as the card value for the dict value.

        value (int): The number of card values in the deck.

        suit (int): The number of suits in the deck.
    """

    def __init__(self):
        """Constructs a new instance of Card.
        
        Args:
            self (Card): An instance of Card.
        """
        self.__suits = {1: "Club",
                        2: "Diamond",
                        3: "Heart",
                        4: "Spade"}

        self.__values = {1: "One",
                         2: "Two",
                         3: "Three",
                         4: "Four",
                         5: "Five",
                         6: "Six",
                         7: "Seven",
                         8: "Eight",
                         9: "Nine",
                         10: "Ten",
                         11: "Jack",
                         12: "Queen",
                         13: "King", }

        self.__value = 1
        self.__suit = 1
        self.shuffle()

    def shuffle(self):
        """Generates a new random suit and card value for the card.
        
        Args:
            self (Card): An instance of Card."""
        self.__value = random.randint(1, 13)
        self.__suit = random.randint(1, 4)

    def get_suit(self):
        """Returns a suit.
        
        Args:
            self (Card): An instance of Card.
        """
        return self.__suit

    def get_suit_string(self):
        """Returns the card suit as a string.
        
        Args:
            self (Card): An instance of Card.
        """
        return self.__suits[self.suit]

    def set_suit(self, value):
        """Sets the card suit to a new number.
        
        Args:
            self (Card): An instance of Card.
        """
        self.__suit = value

    def get_value(self):
        """Returns the card value.
        
        Args:
            self (Card): An instance of Card.
        """
        return self.__value

    def get_value_string(self):
        """Returns the card value as a string.
        
        Args:
            self (Card): An instance of Card.
        """
        return self.__values[self.value]

    def set_value(self, value):
        """Sets the card value to a new number.
        
        Args:
            self (Card): An instance of Card.
        """
        self.__value = value

    def card_name(self):
        """Returns the string expression of a card.
        Example: 'King of Clubs'
        
        Args:
            self (Card): An instance of Card.
        """
        return (f"{self.get_value_string()} of {self.get_suit_string()}s")

    # Properties

    suit = property(get_suit, set_suit)

    value = property(get_value, set_value)


