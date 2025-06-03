# crossing-capstone-project-
A simple crossing capstone project, built using the python's built in turtle graphic library 

🚀 Game Objective
Guide the turtle from the bottom of the screen to the top without getting hit by a car. Reach the top successfully to score a point and increase the game's difficulty.

🎮 Game Controls
Up Arrow (↑) → Move the turtle upward

🛠️ Project Structure & Module Descriptions
main.py
Handles the game setup and main loop:

Initializes screen, turtle, cars, and scoreboard

Runs the game loop:

Generates and moves cars

Detects collisions

Checks for level completion

Increases difficulty by speeding up cars on each level

tortoise.py
Defines the player's character:

python
Copy
Edit
class Tortoise(Turtle):
    """
    Represents the player's turtle character that moves upward on each key press.
    """
move_up() — Moves the turtle up by 10 pixels.

reset_position() — Resets the turtle to the starting position after each level.

car_manager.py
Manages the creation and movement of cars:

python
Copy
Edit
class Car(Turtle):
    """
    Manages car generation, movement, and speed control.
    """
generate_cars() — Randomly creates a new car and positions it on the right edge of the screen.

move_across() — Moves all existing cars from right to left.

increase_speed() — Speeds up the cars as the game progresses.

scoreboard.py
Manages game scoring and end game message:

python
Copy
Edit
class Scoreboard(Turtle):
    """
    Tracks and displays the player's score.
    """
increase_score() — Increments the score when a level is completed.

game_over() — Displays a "Game Over" message when a collision is detected.

📁 Project Files Overview
File	Description
main.py	Main game loop and event handling
tortoise.py	Player turtle logic
car_manager.py	Car creation, motion, and difficulty control
scoreboard.py	Score tracking and game over display

📦 Requirements
Python 3.x

No external libraries — uses only built-in turtle and random

🐞 Issues Encountered
Rapid bounce bug: When a car overlapped with the turtle, the collision detection could trigger multiple times per second due to overlapping frames.

Fix: Improved logic by reducing turtle hitbox size and confirming precise distance checks (distance(car) < 15).

Car motion: Ensured cars are moved frame-by-frame in a list (car_list) inside a loop rather than through a single movement call.

💡 Learning Outcomes
Object-Oriented Programming with classes

Event-driven programming using key bindings

Collision detection and sprite movement with Turtle

Game loop mechanics and progressive difficulty
