from PIL import Image, ImageFilter

image = Image.open("photos\\pic.jpg")

# 1 bit grayscale image
image2 = image.convert("1")

# 8 bit grayscale image (L = Luminosity is brightness normally for people)
image2 = image.convert("L")

# Palette (256 colors only)
image2 = image.convert("P")

# Palette 16 
image2 = image.convert("P", palette = Image.Palette.ADAPTIVE, colors = 16)

image2.show()