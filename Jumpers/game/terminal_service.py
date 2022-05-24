from jumper import jumper

word = ""
hidden_word = ""
hidden_word_string = ""
hidden_word_string = hidden_word_string.join(hidden_word)
wrong_guesses = ""

class TerminalService:
    def __init__(self):
        self.word = ""

    jumper = jumper()

    def display_hidden_word(self, word, hidden_word):
        for i in range (len(word)):
            hidden_word.append("_")
        return(hidden_word) 
    
    def letter_guess(self, prompt):
        
        letter_input = input("\nGuess a letter [a-z]: ")
            
        for i in range (len(word)):
            if letter_input.lower() == word[i]:
                hidden_word.pop(i)
                hidden_word.insert(i, letter_input.upper() + " ")
        
        if letter_input not in word:            
            if letter_input.lower() not in wrong_guesses:
                print(f"\nNope, {letter_input.upper()} is not there!")
                wrong_guesses.append(letter_input.lower())
            else:
                print(f"You have already guessed that {letter_input.lower()}!")
        
        if len(wrong_guesses) > 0:
            print(f"Current wrong guesses: {wrong_guesses}")
                  
        print()
        hidden_word_string = ""
        hidden_word_string = hidden_word_string.join(hidden_word)
        print(hidden_word_string)

        return wrong_guesses

    def game_over(self, is_playing, hidden_word):
        checker = "_ "
        if checker in hidden_word:
            is_playing = True
        else:
            is_playing = False
            print("\nCongratulations! You Win!")
            exit()
        return is_playing

   