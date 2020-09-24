#упражнение 2

import turtle as tt
One = [
    (0, 0), (20, 20), (20, -20)
    ]
Four = [
    (0, 0), (0, 20), (0, 0), (20, 0), (20, 20), (20, -20)
    ]
Seven = [
    (0, 0), (20, 20), (0, 20), (20, 20), (0, 0), (0, -20)
    ]
Zero = [
    (0, 20), (20, 20), (20, 0), (20, -20), (0, -20), (0, 0)
    ]
i = 0

#Функция, рисующая определенную цифру(digit) с отступом d
def number_draw(digit, d):
    tt.goto(40*d, 0)
    tt.pendown()
    for x, y in digit:
        tt.goto(x + 40*d, y)
    tt.penup()
    
tt.shape('turtle') 
for k in [One, Four, One, Seven, Zero, Zero]:
    number_draw(k, i)
    i += 1

tt.done()
