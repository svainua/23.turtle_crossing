from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.left(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)
        
    def go_back(self):
        self.backward(MOVE_DISTANCE)

    def go_left(self):
        self.left(90)
        self.forward(10)
        self.right(90)

    def go_right(self):
        self.right(90)    


