from PIL import Image

bear = Image.open("photos\\saveimg.png")
bird = Image.open("photos\\saveimg.jpg")
img = Image.open("photos\\pic.jpg")

# Masking needs a specific mode : either RGBA 1 or L (other modes won't work)
mask = Image.open("photos\\m.png")
masked = Image.alpha_composite(bear.convert("RGBA"), mask.convert("RGBA"))

# advanced way of using mask 
ye = Image.composite(bird, bear, mask)

ye.show()
