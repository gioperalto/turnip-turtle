from turnip_turtle import TurnipTurtle
import turtle

def collision(a, b):
  return abs(a.xcor() - b.xcor()) < 10 and abs(a.ycor() - b.ycor()) < 10

if __name__ == "__main__":
  space, turnip = turtle.Screen(), turtle.Turtle()
  space.register_shape('images/turnip.gif'), turnip.shape('images/turnip.gif')
  turtles, players = [], open('players.txt').read().split()

  for player in players:
      turtles.append(TurnipTurtle(turtle=turtle, turnip=turnip, name=player, screensize=space.screensize()))

  for turt in turtles:
      turt.info()

  done = False
  while not done:
    for turt in turtles:
      turt.random_turn()
      turt.move()

      if collision(turt.turtle, turnip):
        done = True
        turt.win()
        break

  space.exitonclick()