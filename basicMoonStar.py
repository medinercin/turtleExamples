import turtle
t=turtle.Turtle()

t.speed(10)
t.shape('turtle')
t.color('red','black')
t.color("red")
t.begin_fill()
t.left(90)
t.circle(120)
t.circle(90)
t.forward(70)
for i in range(5):
    t.right(144)
    t.forward(190)
t.end_fill()
print(t.pos())
turtle.done()

