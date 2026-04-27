import os
from PIL import Image, ImageFilter
di = r"C:\Users\Анастасия\Downloads\images-py"
os.makedirs(di, exist_ok=True)
for i in range(1, 6):
    file = r'C:\Users\Анастасия\Downloads\-' + str(i) + ".jpg" #оно не хотело делить видеть кавычку сразу после \, поэтому -
    if os.path.exists(file):
        img = Image.open(file)
        fmg = img.filter(ImageFilter.EDGE_ENHANCE)
        way = os.path.join(di, "fil" + str(i) + ".jpg")
        fmg.save(way)
        print("изменен файл: ", file)
    else:
        print("Файл ", file, " не найден")