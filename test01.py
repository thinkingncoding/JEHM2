import turtle #  모듈
t = turtle.Turtle()
t.shape("turtle")

t.speed(3)

for i in range(4):
    t.forward(100)
    t.left(90)

t.forward(200)

for i in range(3):
    t.forward(100)
    t.left(120)


t.circle(100)
turtle.mainloop()