# Play=True
import turtle
# screen=turtle.Screen()
# screen.bgcolor("blue")
# turtle=turtle.Turtle()
# turtle.shape("turtle")
# turtle.color("green")
# turtle.pensize(50)
# while Play==True:
#   turtle.forward (500)
#   turtle.color("red")
#   turtle.backward (500)
#   Play=True

# # import turtle
# screen = turtle.Screen()
# screen.bgcolor("blue")
# turtle=turtle.Turtle()
# turtle.shape("turtle")
# turtle.pensize(50)
# turtle.color("orange")
# turtle.forward (500)
# turtle.right (90)
# turtle.forward(500)
# turtle.right(90)
# turtle.forward (500)
# turtle.right (90)
# turtle.forward(500)
# turtle.right(90)
# turtle.color("red")
turtle1=turtle.Turtle()
window=turtle.Screen()
window.bgcolor("black")
turtle1.speed(50)
variable=0
def Circle():
  turtle1.color("green")
  turtle1.circle(50)
def Circle2():
  variable=0
  while variable<36:
    turtle1.color("blue")
    turtle1.circle(70)
    turtle1.left(20)
    variable=variable+1
def Square():
  variable=0
  while variable<16:
    turtle1.color("red")
    turtle1.forward(100)
    turtle1.right(90)
    turtle1.forward(100)
    turtle1.right(90)
    turtle1.forward(100)
    turtle1.right(90)
    turtle1.forward(100)
    turtle1.right(10)
    variable=variable+1

def Square2():
  variable=0
  while variable<16:
    turtle1.color("yellow")
    turtle1.forward(150)
    turtle1.right(90)
    turtle1.forward(150)
    turtle1.right(90)
    turtle1.forward(150)
    turtle1.right(90)
    turtle1.forward(150)
    turtle1.right(10)
    variable=variable+1

def Patterns():
  variable=0
  while variable<36:
    Circle()
    variable=variable+1
    turtle1.right(10)
  Circle2()
  Square()
  Square2()

    
window.onkey(Patterns,"a")
window.listen()

