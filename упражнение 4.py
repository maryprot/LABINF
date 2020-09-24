#упражнение 4
import turtle as tt

x, y, dt, Vx, Vy, ay = -350, 0, 0.05, 15, 50, -10

tt.shape('circle')
tt.speed(100)
tt.goto(350, 0)
tt.goto(-350, 0)
for i in range(700):
    x += Vx * dt
    y += Vy*dt + ((ay * dt**2) / 2)
    Vy += ay * dt
    if y <= 0:
        Vy = -0.8 * Vy 
    tt.goto(x, y)
tt.done()
