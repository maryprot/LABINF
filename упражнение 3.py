import turtle as tt

x = 0

# Функция, рисующая определенную цифру(digit) с отступом d
def number_draw(digit, d):
    tt.goto(40*d, 0)
    tt.pendown()
    for x, y in digit:
        tt.goto(x + 40*d, y)
    tt.penup()

    
tt.shape('turtle')

with open('TEXT.txt', 'r') as out:
    for line in out:
        line = line.rstrip()
        A = list(line)
        A = line.split('/')
        for i in range(len(A)):
            A[i] = A[i].split(',') 
            A[i][0] = int(A[i][0])
            A[i][1] = int(A[i][1])
        print(A)
        number_draw(A,x)
        x += 1
        
tt.done()
 
