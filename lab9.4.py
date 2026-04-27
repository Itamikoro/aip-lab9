from PIL import Image, ImageDraw, ImageFont
img = Image.open(r"C:\Users\Анастасия\Downloads\noname.jpg").convert("RGBA")
txt = Image.new('RGBA', img.size, (255, 255, 255, 0))
d = ImageDraw.Draw(txt)
font = ImageFont.load_default(36)

w, h = img.size
x = w / 3
y = h / 2

d.text((x, y), "dont touch", font=font, fill=(255, 255, 255, 255))
wimg = Image.alpha_composite(img, txt)
wimg.convert('RGB').save(r"C:\Users\Анастасия\Downloads\newnoname.jpg")