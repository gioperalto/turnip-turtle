from turnip_turtle import TurnipTurtle
import turtle, sys

def collision(a, b):
  """
  Determines if object a and b are intersecting.
  @param a first object
  @param b second object
  @return True or False
  """
  return abs(a.xcor() - b.xcor()) < 25 and abs(a.ycor() - b.ycor()) < 25

def race(arg):
  """
  Simulates a turtle race between all of the players in players.txt. 
  The objective of this race is to reach the target first.
  @param target the target image to race to (a stationary turtle)
  """
  space, target = turtle.Screen(), turtle.Turtle()
  space.register_shape('images/{}.gif'.format(arg)), target.shape('images/{}.gif'.format(arg))
  turtles, players = [], open('players.txt').read().split()

  for player in players:
      turtles.append(TurnipTurtle(turtle=turtle, target=target, name=player, screensize=space.screensize()))

  for turt in turtles:
      turt.info()

  done = False
  while not done:
    for turt in turtles:
      turt.random_turn()
      turt.move()

      if collision(turt.turtle, target):
        done = True
        turt.win()
        break

  space.exitonclick()

if __name__ == "__main__":
  if len(sys.argv) != 2:
    experiment = 'turnip'
  else:
    experiment = sys.argv[1]

  race(experiment)