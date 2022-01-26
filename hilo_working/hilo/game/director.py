from game.card import Card

"""
Cameron Barrett
Director Class in progress
CSE 210
"""

class Director:
    def __init__(self):
        self.first_card = {}
        self.next_card = {}
        self.is_playing = True
        self.points = 0
        self.total_score = 300

    def start_game(self):
        while self.is_playing:
            self.first_draw()
            self.hilo()
            self.second_draw()
            self.score()
            self.play_again()

    def first_draw(self):
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
        self.draw_card = ""
        self.draw_card = input("Higher or lower? [h/l] ").lower()
        while self.draw_card != "h" and self.draw_card != "l":
            print("\nPlease Type h for Higher or l for Lower")
            self.draw_card = input("Higher or lower? [h/l] ").lower()

    def second_draw(self):
        card2 = Card()
        card2.shuffle()
        card_dict2 = {card2.card_name(): card2.get_value()}
        self.next_card.update(card_dict2)
        card_dict2.clear()

        for key2, value2 in self.next_card.items():
            self.card_value2 = value2
        print(f"Next card was: {key2}")

    def score(self):
        if self.card_value1 < self.card_value2 and self.draw_card == "h":
            self.points = 100
        elif self.card_value1 > self.card_value2 and self.draw_card == "l":
            self.points = 100
        elif self.card_value1 > self.card_value2 and self.draw_card == "h":
            self.points = -75
        elif self.card_value1 < self.card_value2 and self.draw_card == "l":
            self.points = -75
        else:
            self.points = 0
        self.total_score += self.points

        print(f"Your score is: {self.total_score}")
        self.first_card.clear()
        self.next_card.clear()

    def play_again(self):
        if self.is_playing == (self.total_score > 0):
            deal = ""
            deal = input("Play again? [y/n] ").lower()
            while deal != "y" and deal != "n":
                print("\nPlease type y for Yes or N for No.")
                deal = input("Play again? [y/n] ").lower()
            self.is_playing = (deal == "y")
            if deal == "n":
                print(f"Your score is: {self.total_score}\nThanks for playing!")
        else:
            self.is_playing = print("Game Over")