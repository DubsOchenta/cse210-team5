from .hilo_card import Card

class Director:
    def __init__(self):
        self.first_card = []
        self.next_card = []
        self.is_playing = True
        self.points = 0
        self.total_score = 300

    def start_game(self):
        while self.is_playing:
            self.first_deal()
            self.do_updates()
            self.play_again()

    def first_deal(self):
        for i in range(1):
            base_card = Card.draw(self)
            self.first_card.append(base_card)

        for i in range(len(self.first_card)):
            face_card = self.first_card[i]

        print(f"\nThe card is: {face_card}")

        self.draw_card = ""
        while self.draw_card != "h" and self.draw_card != "l":
            self.draw_card = input("Higher or lower? [h/l] ")


    def do_updates(self):
        if not self.is_playing:
            return
        for i in range(1):
            hilo_card = Card.draw(self)
            self.next_card.append(hilo_card)

        for i in range(len(self.first_card)) and range(len(self.next_card)):

        # for i in range(len(self.first_card)):
        #     for i in range(len(self.next_card)):
            card1 = self.first_card[i]
            card2 = self.next_card[i]

            if card1 < card2 and self.draw_card == "h":
                self.points = 100
            elif card1 > card2 and self.draw_card == "l":
                self.points = 100
            elif card1 > card2 and self.draw_card == "h":
                self.points = -75
            elif card1 < card2 and self.draw_card == "l":
                self.points = -75
            else:
                self.points = 0
        self.total_score += self.points

        for i in range(len(self.next_card)):
            dealt_card = self.next_card[i]

        print(f"Next card was: {dealt_card}")
        print(f"Your score is: {self.total_score}")
        self.is_playing = self.total_score > 0

    def play_again(self):
        if not self.is_playing:
            return
        deal = ""
        while deal != "y" and deal != "n":
            deal = input("Play again? [y/n] ")
        self.is_playing = (deal == "y")
