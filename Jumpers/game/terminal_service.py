from jumper import jumper

    
class TerminalService:
    def __init__(self):
        self.word = ""

    jumper = jumper()

    def letter_guess(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        
        letter_input = input("\nGuess a letter [a-z]: ")

        while (len(letter_input.lower()) > 1) or not (letter_input.isalpha()):
            if (len(letter_input.lower()) > 1):
                letter_input = input("\nHow about just one letter?: ")

            if not letter_input.isalpha():
                letter_input = input("\nDo you know what a letter is? Try again: ")



    def write_text(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(text)

   