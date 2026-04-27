from PIL import Image

way = r"C:\Users\Анастасия\Downloads\noname.jpg"
img = Image.open(way)

nsize = (img.width // 3, img.height // 3)
simg = img.resize(nsize)
simg.save(r"C:\Users\Анастасия\Downloads\smallnoname.jpg")

aflip = img.transpose(Image.FLIP_LEFT_RIGHT)
aflip.save(r"C:\Users\Анастасия\Downloads\flip1.jpg")

bflip = img.transpose(Image.FLIP_TOP_BOTTOM)
bflip.save(r"C:\Users\Анастасия\Downloads\flip2.jpg")