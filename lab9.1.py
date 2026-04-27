from PIL import Image


way = r"C:\Users\Анастасия\Downloads\noname.jpg"

try:
    img = Image.open(way)
    print("Размер: ", img.size, "ширина, высота")
    print("Формат: ", img.format)
    print("Цветовая модель: ", img.mode)
    img.show()
except FileNotFoundError:
    print("Файл не найден")