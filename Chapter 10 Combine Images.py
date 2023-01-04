from PIL import Image, ImageChops

bear = Image.open("photos\\saveimg.png")
bird = Image.open("photos\\saveimg.jpg")
img = Image.open("photos\\pic.jpg")

# merging images with image.methods()
new = Image.blend(bear, bird, 100)     # (image1, image2, alpha value{1.0 for default}), both images should be of same size and mode. Higher number can turn it into nightmare 
new1 = Image.composite(bear, bird, Image.new("L", bear.size, 100))      

# image paste 
img.paste(bird, (0,0))
img.paste(bear,(100,100), mask=bear)       # to add transparency, the image must be .png

new.show()
