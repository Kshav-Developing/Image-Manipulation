from PIL import Image 

# Create a new image using scratch by Image.new(format {color}, size {width,height})
image = Image.new("RGBA", (500, 600))

image.show()

# Saving the picture (can be used to change format)
image.save("test_save.png")

# Printing the image attributes 
print(image.size)
print(image.filename)
print(image.format)