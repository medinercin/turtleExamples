from turtle import *

shape("triangle")
color("red", "yellow")
begin_fill()
speed(10)
pensize(5)  # çizgi kalınlığı
for i in range(12):
    pendown()
circle(120, 180)  # yarım daire çizelim
penup()
right(30)
goto(0, 0)
for a in range(12):
    pendown()
circle(120, -180)  # yarım daire çizelim
penup()
right(30)
goto(0, 0)
end_fill()
exitonclick()