from PIL import Image, ImageFilter

image = Image.open("photos\\pic.jpg")

image_boxblur = image.filter(ImageFilter.BoxBlur(radius=10))
image_gaussblur = image.filter(ImageFilter.GaussianBlur(radius=10))
image_unsharp = image.filter(ImageFilter.UnsharpMask(radius=10))

image_unsharp.show()