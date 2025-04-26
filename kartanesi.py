from turtle import *

# Ayarları yapılandıralım
shape("classic")
 # Çizim rengi siyah, iç dolgu rengi pembe

speed(0)
pensize(2)  # Çizgi kalınlığı

# Kar tanesi çizimi
for _ in range(6):  # Kar tanesinin 6 kolu olacak

    forward(100)  # Bir dal çiz
    right(45)
    forward(30)  # Dalın küçük yan çıkıntısı
    backward(30)  # Geri dön
    left(90)
    forward(30)  # Diğer çıkıntı
    backward(30)  # Geri dön
    right(45)
    backward(100)  # Ana dala geri dön

    right(60)  # Bir sonraki kola dön



# Çizimi tamamla
exitonclick()
