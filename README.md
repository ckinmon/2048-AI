# 2048 AI Program

This is a program that simulates and plays the game 2048.  You can play the game without the AI here: http://2048game.com.  
You can read the rules of the game here: https://en.wikipedia.org/wiki/2048_(video_game).

This AI uses the expectiminimax search algorithm to construct a game tree and search for the best possible move. The GameManager enforces a 
.2 seconds time limit to find and execute a move which prevents downtime between moves. The current depth limit with this
time restriction is 3 plys. You can increase the depth limit by increasing (or removing) the time limit restriction.

The AI uses several heuristics to improve speed and optimality. It uses alpha beta pruning to improve the best case
runtime complexity to O(b^(sqrt(n)), where b is the branching factor, and n is the maximum depth of the tree. The AI
also uses four heuristics to calculate the grid value, monotonity, possible merges, and open tiles, and uses weights
to weight each calculation. 

With a depth limit of 3, the AI achieves the winning 2048 game tile around 90% of the time, and achieves the 4096 tile
around 50% of the time. 

This AI is far from optimal. For better testing, the time limit should be removed and the heuristics and weights should be
tested and improved.

## Getting Started

1. Clone a copy of the root folder with all the .py files.
2. Using a command prompt of your choice, navigate to the folder on your computer in which the .py files are containd.
3. Execute the command 'python3 GameManager_3.py' 
4. Watch the AI. 

### Prerequisites And Installation

Python3: https://www.python.org/downloads/

## Running the tests

Here is a demo of the game running on a MacBook Air: https://www.youtube.com/watch?v=3gFNBue07qc

## Authors

Caleb Kinmon
Columbia University, 2020
Computer Science, Intelligent Systems
