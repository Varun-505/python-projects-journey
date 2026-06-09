# Choose Your Own Adventure 

A simple text-based adventure game built with Python where the player's choices determine the outcome of the story.

## Description

In this interactive command-line game, players explore a mysterious forest and make decisions that lead to different endings. Each choice affects the storyline, creating a fun and engaging adventure experience.

The goal is to find the best path and uncover the treasures of the Lost Kingdom.

## Features

* Interactive story-based gameplay
* Multiple decision paths
* Win and lose outcomes
* Personalized experience using the player's name
* Input validation for unexpected choices

## Technologies Used

* Python 3
* Conditional Statements (`if`, `elif`, `else`)
* User Input (`input()`)

## How to Run

1. Open a terminal in the project directory.

2. Run the program:

```bash
python main.py
```

## Example Gameplay

```text
Type your name: Alex

Welcome, Alex, to the Lost Kingdom Adventure!

You wake up in a mysterious forest. Ahead of you are two paths.
Do you go LEFT or RIGHT? left

You discover an ancient castle. The gate is open.
Do you ENTER the castle or WALK away? enter

Inside the castle, you find a magical crown.
You become the ruler of the Lost Kingdom!

YOU WIN!
```

## Story Paths

### Left Path

* Enter the castle → Win 
* Walk away → Game Over ❌

### Right Path

* Take the boat → Win
* Swim across → Game Over ❌

## Project Structure

```text
04_choose_your_own_adventure/
├── main.py
└── README.md
```

## Concepts Practiced

* Variables
* User Input
* String Methods (`lower()`)
* Conditional Logic
* Nested `if` Statements
* Story Design
* Program Flow Control

## Learning Outcomes

Through this project, I learned how to:

* Create branching storylines using nested conditionals
* Handle user choices and input
* Design simple game logic
* Build interactive command-line applications
* Improve user experience with personalized messages

## Future Improvements

* Add more story branches and endings
* Include an inventory system
* Add health points and challenges
* Save player progress
* Convert the game into a graphical application

## Author

Created as part of my Python Projects Journey while learning Python through hands-on projects.
