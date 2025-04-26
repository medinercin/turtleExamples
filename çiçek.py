import turtle
# Ekranı oluştur
screen = turtle.Screen()
screen.title("Çokgen Çiçek Deseni")
# Turtle oluştur
flower = turtle.Turtle()
flower.speed(0)  # Hızlı çizim için
# Fonksiyon: Çokgen çizme
def draw_polygon(sides, length):
    angle = 360 / sides
    for _ in range(sides):
        flower.forward(length)
        flower.left(angle)
# Çiçek deseni çizme
for _ in range(36):  # 36 kez dönecek
    draw_polygon(5, 50)  # 6 kenarlı bir çokgen (altıgen)
    flower.left(10)  # Her çokgen arasında 10 derece döndür
# Çizimi tamamlamak için ekranı açık bırak
screen.mainloop()