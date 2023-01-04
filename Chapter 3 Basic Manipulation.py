from PIL import Image, ImageColor       # Image color for specifying image without rgb

image = Image.open("photos\\pic.jpg")

# rotating image (.rotate(degree))
image_rotate = image.rotate(90)

# rotating and expanding the image so that the image is not cut and changing the bg color (rgb)
image_rotate = image.rotate(70, expand=True, fillcolor=(0, 240, 23))

# changing bg color using ImageColor
image_rotate = image.rotate(70, expand=True, fillcolor=ImageColor.getcolor("blue", "RGB"))

# cropping an image (image.crop(left_x, top_y, right_x, bottom_y))
image_crop = image.crop((0,0,1100,700))

# flipping the image 
image_flip_horizontal = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
image_flip_vertical = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

# resize the image (width, height)
image_resize = image.resize((300,500))

image_flip_horizontal.show()
image_flip_vertical.show()
image_crop.show()
image_rotate.show()
image_resize.show()