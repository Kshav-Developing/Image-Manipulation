from PIL import Image, ImageEnhance

image = Image.open("photos\\pic.jpg")

# Create an enhancer
bright_enhance = ImageEnhance.Brightness(image)

# applying the enhancer (add 0 in the argument for black and white image)
image2 = bright_enhance.enhance(3)
image2.show()