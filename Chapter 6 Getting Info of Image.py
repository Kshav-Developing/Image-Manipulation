from PIL import Image, ImageFilter

image = Image.open("photos\\pic.jpg")


print(image.getpixel((0,1)))    # Tells the color of a pixel of specified position
print(image.mode)   # Tells the info about the color format in image
# print(image.getcolors(maxcolors = image.size[0] * image.size[1]))    # Tells about all the colors used in every pixel in terms of list (no.times used,[r,g,b])
