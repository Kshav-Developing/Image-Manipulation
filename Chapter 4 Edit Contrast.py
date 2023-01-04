from PIL import Image, ImageEnhance

image = Image.open("photos\\pic.jpg")

# Create an enhancer
contrast_enhance = ImageEnhance.Contrast(image)

# applying the enhancer
image2 = contrast_enhance.enhance(3)
image2.show()