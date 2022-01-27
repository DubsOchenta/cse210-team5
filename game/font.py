
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
        print("##     ## ####  ######   ##     ## ########  #######   ###  ###")
        print(f"\033[0m")