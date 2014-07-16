#alicia leslie
#turtle

import turtle

#triangle
turtle.pensize(3)
turtle.penup()
turtle.goto(-200,-50)
turtle.pendown()
turtle.circle(40,steps=3)

#square
turtle.penup()
turtle.goto(-100,-50)
turtle.pendown()
turtle.circle(40,steps=4)

#pentagon
turtle.penup()
turtle.goto(0,-50)
turtle.pendown()
turtle.circle(40,steps=5)

#hexagon
turtle.penup()
turtle.goto(100,-50)
turtle.pendown()
turtle.circle(40,steps=6)

#circle
turtle.penup()
turtle.goto(200,-50)
turtle.pendown()
turtle.circle(40)

turtle.done()
