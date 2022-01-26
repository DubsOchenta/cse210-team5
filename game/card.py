
# Card Class
# CSE210 By Robert Odell

import random


class Card:
    """
     Class represents one card

     ...

     Attributes
     -----------

     __values = contains a dictionary with all values
     
     __suits = contains a dictionary with all suits

     __value = (between 1-13)
     
     __suit = (between 1-4)

     Methods
     ---------

     shuffle = randomly change value and suit of card
     
     get_suit = return suit
     
     get_suit_string = returns the card suit as a string
     
     set_suit = set suit to new #
     
     get_value = return value
     
     get_value_string = returns the card value as a string
     
     set_value = set value to new #
     
     card_name = returns the card name as a string ex:'King of Clubs'

     Properties
     ----------

     value = card value (1-13)

     suit = card suit (1-4)

    """

    def __init__(self):
        # Dict - suits
        self.__suits = {1: "Club",
                        2: "Diamond",
                        3: "Heart",
                        4: "Spade"}

        # Dict - values
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

    # Set value to random number

    def shuffle(self):
        self.__value = random.randint(1, 13)
        self.__suit = random.randint(1, 4)

    # Returns card suit

    def get_suit(self):
        return self.__suit

    # Returns the card suit as a string

    def get_suit_string(self):

        return self.__suits[self.suit]

    # Sets card suit

    def set_suit(self, value):
        self.__suit = value

    # Returns card value

    def get_value(self):
        return self.__value

    # Returns card value as a string

    def get_value_string(self):

        return self.__values[self.value]

    # Sets card value

    def set_value(self, value):
        self.__value = value

    # Returns the string expression of a card
    # Example: 'King of Clubs'

    def card_name(self):
        return (f"{self.get_value_string()} of {self.get_suit_string()}s")

    # Properties

    suit = property(get_suit, set_suit)

    value = property(get_value, set_value)


