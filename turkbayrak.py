import turtle
screen=turtle.Screen()
screen.title("türk bayrağı")
screen.bgcolor("white")

bayrak=turtle.Turtle()
bayrak.width(3)
bayrak.speed(0)
def dikdortgen_cizim():
    bayrak.penup()
    bayrak.goto(0,0)
    bayrak.pendown()
    bayrak.color("red")
    bayrak.begin_fill()
    for i in range(2):
        bayrak.forward(200)
        bayrak.right(90)
        bayrak.forward(150)
        bayrak.right(90)
    bayrak.end_fill()
def hilal_ciz():
    #dış daire
    bayrak.penup()
    bayrak.goto(70,-120)
    bayrak.pendown()
    bayrak.color("white")
    bayrak.begin_fill()
    bayrak.circle(40)
    bayrak.end_fill()
    #iç daire
    bayrak.penup()
    bayrak.goto(90, -110)
    bayrak.pendown()
    bayrak.color("red")
    bayrak.begin_fill()
    bayrak.circle(30)
    bayrak.end_fill()
def yildiz_ciz():
    bayrak.penup()
    bayrak.goto(110, -70)
    bayrak.pendown()
    bayrak.color("white")
    bayrak.begin_fill()
    for i in range(5):
        bayrak.forward(50)
        bayrak.right(144)
    bayrak.end_fill()
dikdortgen_cizim()
hilal_ciz()
yildiz_ciz()
screen.mainloop()

