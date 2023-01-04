from PIL import Image, ImageFilter

image = Image.open("photos\\pic.jpg")

# Changing a single pixel color using .putpixel((pixelx, pixely), (r,g,b))
image.putpixel((2, 2), (255,0,0))

# Changing large number of pixels
for x in range(image.size[0]) : 
    image.putpixel((x,100), (0,255,0))

image.show()