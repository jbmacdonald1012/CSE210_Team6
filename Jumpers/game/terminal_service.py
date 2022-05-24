from jumper import jumper
    
class TerminalService:
    def __init__(self):
        self.word = ""

    jumper = jumper()

    
    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        letter_guess = input("Guess a letter [a-z] ")
        return input(prompt)

    def write_text(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(text)

   