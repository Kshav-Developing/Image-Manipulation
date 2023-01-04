from PIL import Image, ImageEnhance

image = Image.open("photos\\pic.jpg")

# Create an enhancer
sharp_enhance = ImageEnhance.Sharpness(image)

# applying the enhancer (add 0 in the argument for black and white image)
image2 = sharp_enhance.enhance(50)
image2.show()