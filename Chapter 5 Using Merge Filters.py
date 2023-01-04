from PIL import Image, ImageFilter, ImageEnhance

image = Image.open("photos\\pic.jpg")

image_enh = ImageEnhance.Brightness(image)
image2 = image_enh.enhance(5)

image3 = ImageEnhance.Sharpness(image2)
image4 = image3.enhance(20)

image4.show()