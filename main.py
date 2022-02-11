import turtle

etch = turtle.Turtle()
etch_screen = turtle.Screen()

def up():
  etch.forward(10)

def down():
  etch.backward(10)

def left():
  etch.setheading(etch.heading() + 10)

def right():
  etch.setheading(etch.heading() - 10)

def clear():
  etch.clear()
  etch.penup()
  etch.home()
  etch.pendown()

def undo():
  etch.undo()


etch_screen.onkey(fun=up, key="Up")
etch_screen.onkey(fun=down, key="Down")
etch_screen.onkey(fun=left, key="Left")
etch_screen.onkey(fun=right, key="Right")
etch_screen.onkey(fun=clear, key="c")
etch_screen.onkey(fun=undo, key="z")


etch_screen.listen()
etch_screen.exitonclick()