#упражнение 1

from random import *
import turtle

#функция броуновского движения: вперед на x, поворот вправо на угол a
def broun(x, a):
    turtle.forward(x)
    turtle.right(a)
    
turtle.shape('turtle')
turtle.speed(100)
turtle.color('red')

for i in range(100):
    broun(randint(1, 20), randint(-360, 360))

turtle.done
