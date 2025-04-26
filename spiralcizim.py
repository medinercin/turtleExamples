import turtle
# Ekranı oluştur
screen = turtle.Screen()
screen.title("Spiral Çizimi")
# Turtle oluştur
spiral = turtle.Turtle()
spiral.speed(0)  # Maksimum hız
# Spiral çizme
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
for i in range(100):  # 100 adımda çizim
    spiral.color(colors[i % len(colors)])  # Renkleri sırayla değiştir
    spiral.forward(i * 2)  # İleriye git
    spiral.left(59)  # 59 derece sola dön
# Çizimi tamamlamak için ekranı açık bırak
screen.mainloop()