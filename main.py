# ---- import libraries -----
from turtle import Screen
from tortoise import Tortoise
from car_manager import CarManager
from scoreboard import Scoreboard
import time

# ---- CONSTANTS ----
S_WIDTH = 400   # Width of the screen
S_HEIGHT = 400  # Height of the screen

# --- OBJECT INSTANTIATION ---
tortoise = Tortoise()       # Player character that moves up
cars = CarManager()                # Manages all car creation and movement
scoreboard = Scoreboard()   # Tracks and displays the score/level

# ---- SETUP THE GAME SCREEN ----
screen = Screen()
screen.title("Crossing Capstone Game")  # Title of the window
screen.bgcolor("white")                 # Background color
screen.setup(width=S_WIDTH, height=S_HEIGHT)  # Set screen dimensions
screen.tracer(0)  # Turn off auto-refresh to allow manual screen updates (smoother animation)
screen.listen()   # Enable keyboard listening for player control

# ---- KEYBOARD CONTROL ----
screen.onkey(tortoise.move_up, "Up")  # Move the tortoise up when "Up" key is pressed

# ---- MAIN GAME LOOP ----
is_game_on = True
while is_game_on:
    time.sleep(0.1)         # Controls game speed (affects frame rate)
    screen.update()         # Refresh screen after all updates
    cars.generate_cars()    # Randomly creates new cars
    cars.move_all_cars()      # Move all cars to the left

    # -- DETECT COLLISION BETWEEN TORTOISE AND CARS --
    for car in cars.car_list:
        if tortoise.distance(car) < 15:
            is_game_on = False         # Stop the game
            scoreboard.game_over()     # Display "Game Over"

    # --- CHECK IF TORTOISE REACHES THE TOP (LEVEL COMPLETED) ---
    if tortoise.ycor() > S_HEIGHT / 2:
        tortoise.reset_position()      # Move tortoise back to start
        scoreboard.increase_score()    # Increase score or level
        cars.increase_speed()          # Speed up cars for next level

# ---- EXIT CLEANLY ON MOUSE CLICK ----
screen.exitonclick()
