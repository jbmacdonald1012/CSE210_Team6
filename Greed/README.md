# GREED
Greed is a game in which the player seeks to gather as many falling gems as possible. The game continues as long as the player wants more!

---
## Getting Started
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 __main__.py 

py __main__.py (on Windows or if above command doesn't work)
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- Greed               (source code for game)
  +-- game              (specific classes)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
Python 3.8.0

## Authors

Victor Lopez
Alberto Almada
Shawn Jensen
Jason Macdonald


Folders:
  --Greed
    -- Game
      -- __main__.py

      -- Casting - Shawn
        -- actor.py
        -- score.py
        -- cast.py

      -- Directing - Victor
        --director.py

      -- Services - Jason
        --keyboardService.py
        --videoService.py

      -- Shared - 
        -- color.py
        -- point.py



What do we need:

Objects:
-Window: 600 x 900
-Gems:  ( * )
-Rocks: ( o )
-Player: ( # )
-Score: number
-Colors: random colors
-Banner: Greed

Behavior: 
-Change Player position (Left and Right at bottom of screen)
-Change Gem position
  -Clear previous gem position once they move
-Change Rock position
  -Clear previous rock position once they move
-Update score
-Randomly generate gems at top
-Randomly generate rocks at top
-Gems disappear at the bottom (if not caught)
-Rocks disappear at the bottom (if not touched)
-Gems disappear if caught
-Rocks disappear if touched
-Game loop (as long as the window is open this loop runs)
-Close window (close the window and release the resources)


