
class Font:
    """Class to print the game title when the game starts.
    
    Attributes:
        yellow_text (str): A string containing ACSII code.
        red_text (str): A string containing ACSII code.
    """
    def __init__(self):
        """Creates a new instance of Font.
        
        Args:
            self (Font): An instance of Font.
        """
        self.yellow_text = "\033[1;33m"
        self.red_text = "\033[1;31m"
        self.green_text = "\033[1;32m"
        self.blue_text = "\033[1;34m"
        self.clear_color = "\033[0m"  

    def print_title(self):
        """Prints the game title to the screen.
        
        Args:
            self (Font): An instance of Font.
        """
        print(f"{self.yellow_text}##     ## ####  ######   ##     ## ##        #######  ##      ## ")
        print("##     ##  ##  ##    ##  ##     ## ##       ##     ## ##  ##  ##")
        print("##     ##  ##  ##        ##     ## ##       ##     ## ##  ##  ##")
        print("#########  ##  ##   #### ######### ##       ##     ## ##  ##  ## ")
        print("##     ##  ##  ##    ##  ##     ## ##       ##     ## ##  ##  ##")
        print("##     ##  ##  ##    ##  ##     ## ##       ##     ## ##  ##  ## ")
        print(f"##     ## ####  ######   ##     ## ########  #######   ###  ###{self.clear_color}")

    def print_instructions(self):
        print(f"""\n{self.blue_text}You start out with 300 points and a randomly chosen starting card. 
Then you are asked a simple question: "h" for High or "l" for Low. 
Each time you guess correctly, you get 100 points, Woohoo! 
But if you guess wrong, well, say goodbye to 75 points from your score. 
As long as your score stays above zero you can keep playing. 
But, If not then it is GAME-OVER.

Let's start! {self.clear_color} """)
