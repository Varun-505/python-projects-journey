# Rock Paper Scissors 🎮

A command-line implementation of the classic Rock Paper Scissors game built with Python. Play against the computer, track your wins, and see the final score when you quit.

## Description

This project allows a user to play Rock Paper Scissors against the computer. The computer randomly selects a move, and the game determines whether the player wins, loses, or ties based on the standard rules.

The game keeps track of both the user's and the computer's wins throughout the session.

## Features

* Play against a computer opponent
* Random computer choices
* Win, loss, and tie detection
* Score tracking
* Input validation
* Exit the game anytime with `Q`

## Technologies Used

* Python 3
* Built-in `random` module

## How to Run

1. Open a terminal in the project directory.

2. Run the program:

```bash
python main.py
```

## Example Gameplay

```text
Type Rock/Paper/Scissors or Q to quit: rock
Computer picked scissors.
you won!

Type Rock/Paper/Scissors or Q to quit: paper
Computer picked paper.
It's a tie!

Type Rock/Paper/Scissors or Q to quit: scissors
Computer picked rock.
you lost!

Type Rock/Paper/Scissors or Q to quit: q

You won 1 times.
The computer won 1 times.
Goodbye!
```

## Game Rules

* Rock beats Scissors
* Scissors beats Paper
* Paper beats Rock
* Matching choices result in a tie

## Project Structure

```text
03_rock_paper_scissors/
├── main.py
└── README.md
```

## Concepts Practiced

* Variables
* Lists
* User Input
* While Loops
* Conditional Statements
* Random Number Generation
* Score Tracking
* Basic Game Logic

## Learning Outcomes

Through this project, I learned how to:

* Build an interactive command-line application
* Validate user input
* Use Python's `random` module
* Implement game logic with conditionals
* Track statistics using variables
* Create a continuous game loop

## Future Improvements

* Best-of-three mode
* Match history
* Difficulty levels
* Graphical User Interface (GUI)
* Save scores to a file

## Author

Created as part of my Python Projects Journey while learning Python through hands-on projects.
