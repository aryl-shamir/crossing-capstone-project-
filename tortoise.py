from turtle import Turtle

# Constant for starting position at the bottom center of the screen
STARTING_POSITION = (0, -175)
MOVE_DISTANCE = 10  # Distance moved per key press

class Tortoise(Turtle):
    """
    Represents the player's character in the Crossing Capstone Game.
    The turtle moves vertically upward and resets position upon leveling up.
    """

    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape('turtle')
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.penup()
        self.left(90)  # Rotate turtle to face upward
        self.goto(STARTING_POSITION)

    def move_up(self):
        """
        Moves the turtle upward by a fixed amount.
        Triggered by the UP arrow key.
        """
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        """
        Resets the turtle's position to the starting point.
        Called after each level is completed.
        """
        self.goto(STARTING_POSITION)
