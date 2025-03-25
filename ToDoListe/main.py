from PIL import Image

img = Image.open("icon.webp")
img.save("icon.ico", format="ICO", sizes=[(16, 16), (32, 32), (64, 64), (128, 128), (256, 256)])


