from turtle import Turtle
import random

# List of simple colors for car selection
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "crimson"]

class CarManager:
    """
    Manages a collection of car objects for the Crossing Capstone Game.
    Handles creation, movement, and speed adjustments of cars.
    """

    def __init__(self):
        self.car_list = []              # List to hold all cars on screen
        self.moving_distance = 2        # Initial car movement speed

    def generate_cars(self):
        """
        Randomly creates a new car and adds it to the car list.
        Uses a 1-in-7 chance to reduce car generation rate for balance.
        """
        random_chance = random.randint(1, 7)
        if random_chance == 1:
            car = Turtle()
            car.shape('square')
            car.shapesize(stretch_wid=0.2, stretch_len=1)
            car.penup()
            car.color(random.choice(colors))
            car.goto(x=200, y=random.randint(-165, 165))
            self.car_list.append(car)

    def move_all_cars(self):
        """
        Moves all existing cars leftwards across the screen.
        """
        for car in self.car_list:
            car.backward(self.moving_distance)

    def increase_speed(self):
        """
        Increases the movement speed of all cars.
        Called whenever the player levels up.
        """
        self.moving_distance += 1
