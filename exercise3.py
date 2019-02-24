# По введенным пользователем координатам двух точек
# вывести уравнение прямой вида y=kx+b,
# проходящей через эти точки.

x1 = int(input("Enter x coordinate of first point: "))
y1 = int(input("Enter y coordinate of first point: "))
x2 = int(input("Enter x coordinate of second point: "))
y2 = int(input("Enter y coordinate of second point: "))
k = (y2 - y1)/(x2 - x1)                         # не стал заморачиваться с правильным оформлением,
b = y2 - x2 * k                                 # поэтому возможны приколы типа y = 0x + -1
print("y = {}x + {}".format(int(k), int(b)))