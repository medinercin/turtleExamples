import turtle
# Ekranı oluştur
screen = turtle.Screen()
screen.title("Renkli Daireler")
# Turtle oluştur
circle_drawer = turtle.Turtle()
circle_drawer.speed(5)
# Renk listesini tanımla
colors = ['red', 'blue', 'green', 'yellow', 'purple']
# Daireler çiz
for color in colors:
    circle_drawer.color(color)
    circle_drawer.circle(50)  # Yarıçapı 50 olan bir daire çiz
    circle_drawer.penup()  # Çizimi kaldır
    circle_drawer.forward(100)  # Bir sonraki daire için pozisyon değiştir
    circle_drawer.pendown()  # Çizimi tekrar başlat
# Çizimi tamamlamak için ekranı açık bırak
screen.mainloop()
