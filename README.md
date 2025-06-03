# 🐢 Crossing Capstone Game

A simple arcade-style game inspired by *Frogger*, built using Python’s built-in `turtle` graphics library.  
The player controls a turtle character trying to cross a road while avoiding incoming cars.  
The game gets harder with each level as the car speed increases.

---

## 🚀 Game Objective

Guide the turtle from the bottom of the screen to the top without getting hit by a car.  
Reach the top successfully to score a point and increase the game's difficulty.

---

## 🎮 Game Controls

- `Up Arrow (↑)` → Move the turtle upward

---

## 🛠️ Project Structure & Module Descriptions

### `main.py`

Handles the game setup and main loop:

- Initializes screen, turtle, cars, and scoreboard
- Runs the game loop:
  - Generates and moves cars
  - Detects collisions
  - Checks for level completion
- Increases difficulty by speeding up cars on each level

---

### `car_manager.py`

Manages the generation of the cars accross the screen and it behaviors. 

---
### `car_manager.py`
Manages game scoring and end game message:

---
## 💡 Learning Outcomes
Object-Oriented Programming with classes

Event-driven programming using key bindings

Collision detection and sprite movement with Turtle

Game loop mechanics and progressive difficulty.


