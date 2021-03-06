import random
from PIL import Image, ImageDraw
print('оберіть тип перетворення!')
print('0 - відтінки сірого')
print('1 - серпія')
print('2 - негатив')
print('3 - зашумлення')
print('4 - зміна яскравості')
print('5 - монохромне зображення')
mode = int(input('mode:')) # обрати тип перетворення зображення за номером.
image = Image.open("start.jpg") # відкриття файлу зображення.
draw = ImageDraw.Draw(image) # створення інструменту для малювання
width = image.size[0] # визначення ширини картинки
height = image.size[1] # визначення висоти картинки
pix = image.load() # отримання значень пікселей для картинки
print(pix[1, 1][1])
print(pix[1,1])
#--------------------- відтінкі сірого ----------------------
if (mode == 0):
	print('------- триває перетворення --------------')
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = (a + b + c) // 3   # усередненя пікселів
			draw.point((i, j), (S, S, S))
#--------------------- серпія  ----------------------
if (mode == 1):
	print('------- ведіть коефіціент серпії --------------')
	depth = int(input('depth:'))
	print('------- триває перетворення --------------')
	for i in range(width):
		for j in range(height):  # підрахунок середнього значення кольорової гами - перетворення з коефіціентом
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = (a + b + c) // 3
			a = S + depth * 2
			b = S + depth
			c = S
			if (a > 255):
				a = 255
			if (b > 255):
				b = 255
			if (c > 255):
				c = 255
			draw.point((i, j), (a, b, c))
# ----------------------- негатив --------------------------
if (mode == 2):
	print('------- триває перетворення --------------')
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			draw.point((i, j), (255 - a, 255 - b, 255 - c)) # від кожного пікселя вичитається 256 - макс. значення для кольору
# --------------------------- зашумлення ------------------------
if (mode == 3):
	print('------- введіть коефіціент шуму --------------')
	factor = int(input('factor:'))
	print('------- триває перетворення --------------')
	for i in range(width):
		for j in range(height):
			rand = random.randint(-factor, factor)
			a = pix[i, j][0] + rand   # додавання рандомного числа
			b = pix[i, j][1] + rand
			c = pix[i, j][2] + rand
			if (a < 0):
				a = 0
			if (b < 0):
				b = 0
			if (c < 0):
				c = 0
			if (a > 255):
				a = 255
			if (b > 255):
				b = 255
			if (c > 255):
				c = 255
			draw.point((i, j), (a, b, c))
# --------------------------- зміна яскравості  ------------------------
if (mode == 4):
	print('введіть діапазон зміни яскравості: -100, +100')
	factor = int(input('factor:')) # наприклад в діапазоні +100, -100
	print('------- триває перетворення --------------')
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0] + factor  # одавання яскравості
			b = pix[i, j][1] + factor
			c = pix[i, j][2] + factor
			if (a < 0):
				a = 0
			if (b < 0):
				b = 0
			if (c < 0):
				c = 0
			if (a > 255):
				a = 255
			if (b > 255):
				b = 255
			if (c > 255):
				c = 255
			draw.point((i, j), (a, b, c))
# --------------------------- монохромне зображення ------------------------
if (mode == 5):
	print('------ введіть коефіціент розрізнення, в діапазоні 50-100 ----------')
	factor = int(input('factor:'))
	print('------- триває перетворення --------------')
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = a + b + c
			if (S > (((255 + factor) // 2) * 3)): # рішення до якого з 2 кольорів поточне значення кольору ближче
				a, b, c = 255, 255, 255
			else:
				a, b, c = 0, 0, 0
			draw.point((i, j), (a, b, c))
# --------------------------- запис до трансформованого файлу ------------------------

image.save("stop.jpg", "JPEG")
del draw
print('------- перетворення завершене до файлу stop.jpg --------------')