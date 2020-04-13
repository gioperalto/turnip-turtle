import numpy as np

class TurnipTurtle:
    def __init__(self, turtle, turnip, name, screensize):
        self.name, self.step, self.direction = name, 30, 90
        self.colors = ['red', 'orange', 'green', 'blue', 'purple', 'black']
        self.width, self.height = screensize
        self.x, self.y  = self.random_spot(self.width), self.height,

        self.turnip = turnip
        self.turtle = turtle.Turtle()
        self.turtle.shape('turtle'), self.turtle.penup()
        self.turtle.color(self.colors[np.random.randint(len(self.colors))])
        self.turtle.setheading(self.direction)
        self.turtle.setx(np.random.randint(-self.x/1.5, self.x/1.5))
        self.turtle.sety(-self.y + 50)

    def random_spot(self, axis_length):
        return np.random.randint(axis_length)

    def random_turn(self):
        self.turtle.setheading(self.direction+np.random.randint(-self.step,self.step))

    def face_turnip(self):
        self.turtle.setheading(self.turtle.towards(self.turnip))

    def move(self):
        step = np.random.randint(self.step)

        if self.turtle.ycor() >= self.height or self.turtle.ycor() <= -self.height or \
            self.turtle.xcor() <= -self.width or self.turtle.xcor() >= self.width:
            self.face_turnip()
            self.turtle.forward(step)
        else:
            self.turtle.forward(step)

    def win(self):
        style = ('Courier', 50, 'bold')
        self.turtle.write('{} wins!'.format(self.name), font=style, align='center')



    def info(self):
        print('Turle info:\nName:\t"{}"\nx:\t{}\ny:\t{}'.format(self.name, self.x, self.y))
