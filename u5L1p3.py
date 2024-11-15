import turtle

t = turtle.Turtle()

for i in range(3):
  t.forward(100)
  t.left(120)
  turtle.penup()
  turtle.goto(100,100)
  turtle.pendown()
  turtle.dot(20, "pink")
  turtle.penup()
