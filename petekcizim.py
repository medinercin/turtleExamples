import turtle

# Ekranı oluştur
screen = turtle.Screen()
screen.title("Petek Deseni")
# Turtle oluştur
honeycomb = turtle.Turtle()
honeycomb.speed(3)


# Fonksiyon: Altıgen çizme
def draw_hexagon(size):
    for _ in range(6):
        honeycomb.forward(size)
        honeycomb.left(60)

    # Petek deseni oluşturma


for row in range(5):  # Satırlar
    for col in range(5):  # Sütunlar
        honeycomb.penup()
        honeycomb.goto(col * 70, row * 52)  # Altıgenler arası boşluk
        honeycomb.pendown()
        draw_hexagon(50)

    # Çizimi tamamlamak için ekranı açık bırak
screen.mainloop()