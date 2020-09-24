from random import *
import turtle as tt

tt.up()
tt.goto(-200, 200)
tt.down()

for i in range(4):
    tt.forward(400)
    tt.right(90)
tt.hideturtle()

number_of_turtles = 20

pool = [tt.Turtle(shape='circle') for i in range(number_of_turtles)]

for unit in pool:
    unit.penup()
    unit.speed(200)
    unit.color('green')
    unit.turtlesize(0.5, 0.5)
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.seth(randint(0, 360))
            
while True:
    for unit in pool:
        unit.forward(randint(1, 10))
        if abs(unit.xcor()) >= 200:
            unit.seth(180 - unit.heading())
            unit.forward(10)
        if abs(unit.ycor()) >= 200:
            unit.seth(360 - unit.heading())
            unit.forward(10)
