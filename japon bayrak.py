from turtle import *

shape('blank')
pensize(5)
for i in range(2): #çerçeveyi çizelim
    forward(150)
    right(90)
    forward(100)
    right(90)
pensize(1)
pencolor("red") #kalem rengi
penup() #kalemi kaldır
goto(75,-80) #daire pozisyonu
pendown() #kalemi koy
fillcolor("red") #daire çizip kırmızıya boya
begin_fill()#boyamaya başla
circle(30)
end_fill()
done()