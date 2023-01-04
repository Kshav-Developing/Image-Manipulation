from PIL import Image

# create new image by importing 
image = Image.open("photos\\pic.jpg")

# alternate method to import an image (a bit more clearer)
with Image.open("photos\\pic.jpg") as image : 
    image.show()

#   show the image
image.show()


