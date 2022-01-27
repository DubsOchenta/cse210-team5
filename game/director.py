"""
Tylor Perry
Cameron Barrett
Robert Odell
Wilson Romero
Nourcel Kaniki
Director Class
CSE 210
"""
from .card import Card
from .font import Font


class Director:
    """A person who directs the game.

    The director controls the sequece of game play.

    Attributes:
    -----------
        first_card (dict{card1.card_name(): card1.get_value()}): A dictionary
        with card1.card_name as the key and card1.get_value as the value.

        next_card (dict{card2.card_name(): card2.get_value()}): A dictionary
        with card2.card_name as the key and card2.get_value as the value.

        is_playing (boolean): Whether or not the game is being played.

        points (int): The amount of points scored during a round.

        total_score (int): The score for the entire game.

        font (class): An instance of Font class.
        
        font_color (string): A blank string that will hold the color depending on the score.
        
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
        -----
            self (Director): an instance of Director.
        """
        self.first_card = {}
        self.next_card = {}
        self.is_playing = True
        self.points = 0
        self.total_score = 300
        self.font = Font()
        self.font_color = ""

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
        -----
            self (director): an instance of Director.
        """

        self.font.print_title()
        self.font.print_instructions()
        while self.is_playing:
            self.first_draw()
            self.hilo()
            self.second_draw()
            self.score()
            self.play_again()

    def first_draw(self):
        """Generates the first random card and displays it to the player.
        
        Args:
        -----
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        card1 = Card()
        card1.shuffle()
        card_dict1 = {card1.card_name(): card1.get_value()}
        self.first_card.update(card_dict1)
        card_dict1.clear()

        for key1, value1 in self.first_card.items():
            self.card_value1 = value1
        print(f"\nThe card is: {key1}")

    def hilo(self):
        """Asks the user if the next card will be higher or lower.
        
        Args:
        -----
            self (Director): An instance of Director.
        """
        self.draw_card = ""
        self.draw_card = input(f"{self.font.yellow_text}Higher or lower? [h/l] {self.font.clear_color}").lower()
        while self.draw_card != "h" and self.draw_card != "l":
            print(f"\n{self.font.yellow_text}Please Type h for Higher or l for Lower")
            self.draw_card = input(f"Higher or lower? [h/l] {self.font.clear_color}").lower()

    def second_draw(self):
        """Generates the second random card and displays it to the player.
        
        Args:
        -----
            self (Director): An instance of Director.
        """
        card2 = Card()
        card2.shuffle()
        card_dict2 = {card2.card_name(): card2.get_value()}
        self.next_card.update(card_dict2)
        card_dict2.clear()

        for key2, value2 in self.next_card.items():
            self.card_value2 = value2
        print(f"Next card was: {key2}")

    def score(self):
        """Updates the players score and displays the score to the player.
        
        Args:
        -----
            self (Director): An instance of Director.
        """
        if self.card_value1 < self.card_value2 and self.draw_card == "h":
            self.points = 100
            self.font_color = self.font.green_text
        elif self.card_value1 > self.card_value2 and self.draw_card == "l":
            self.points = 100
            self.font_color = self.font.green_text
        elif self.card_value1 > self.card_value2 and self.draw_card == "h":
            self.points = -75
            self.font_color = self.font.red_text
        elif self.card_value1 < self.card_value2 and self.draw_card == "l":
            self.points = -75
            self.font_color = self.font.red_text
        else:
            self.points = 0
            self.font_color = self.font.blue_text
        self.total_score += self.points

        print(f"{self.font_color}Your score is: {self.total_score}{self.font.clear_color}")
        self.first_card.clear()
        self.next_card.clear()

    def play_again(self):
        """Asks the player if they want to play again.
        
        Args:
        -----
            self (Director): An instance of Director.
        """
        if self.is_playing == (self.total_score > 0):
            deal = ""
            deal = input("Play again? [y/n] ").lower()
            while deal != "y" and deal != "n":
                print("\nPlease type y for Yes or N for No.")
                deal = input("Play again? [y/n] ").lower()
            self.is_playing = (deal == "y")
            if deal == "n":
                print(f"Your score is: {self.total_score}\n {self.font.blue_text} Thanks for playing!{self.font.clear_color}")
        else:
            self.is_playing = print("Game Over")

            
