# Jumper
---
Jumper is  game that the player seeks to solve a puzzle by guessing the letters of a secret word.
The words are choosen from a secret list, and if the player choose a correct letter the letter is revealed.
If the player guess a incorrect letter, a line is cut on the player's parachute. If the player discover with his guesses the game is over, and with the no more line's in parachute, the game is over. 
This game is a variation of Hangman game.

======================================================================

## Getting Started
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 __main__.py 

py __main__.py (on Windows or if above command doesn't work)
```        

## Project Structure
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- Jumpers             (source code for game)
  +-- game              (specific classes)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
* Python 3.8.0

=======================================================================
## Authors: 
Victor Lopez
Shawn Jensen
Jason Macdonald
Alberto Almada

=======================================================================

Classes needed: 

    Word - Alberto
        creating list of words
            - words cannot be manipulated by other methods/classes

    Terminal Service - Shawn
        Read inputs
        Validate
        Create Output

    Jumper - Victor
        Represents the jumper

        jumper = ['----', '/____\', '\    /', '\  /', 'O','/|\', '/ \', '^^^^^^^']

    Director: - Jason
        startGame
        Gameplay
        inputs
        outputs

========== DIRECTOR ===========
word : Word
is_playing: boolean
validate : Validate
terminalService : TerminalService

------------------------------
startGame() : None
_getInputs() : None
_doUpdates() : None
_doOutputs() : None


======== TERMINAL SERVICE ========

-----------------------------------

Class word : get word
readInput : string
validate : boolean
createOuput : string


======== Jumper ===========

Create List [['----', '/____\', '\    /', '\  /', 'O','/|\', '/ \', '^^^^^^^']]
draw : the jumper and parachute
delete : parachute by index

---------------------------


======== WORD ========

Create list [words]
random choice : get word
    use access modiifer to make private

----------------------



