import turtle
turtle.Screen().bgcolor("Green")
turtle.Screen().setup(300, 400)
p = turtle.Turtle()
numberofsides = 5
sidelength = 60
angle = 360 / numberofsides
for i in range(numberofsides):
    p.forward(sidelength)
    p.right(angle)
turtle.done()