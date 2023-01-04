from PIL import Image, ImageChops

bear = Image.open("photos\\saveimg.png")
bird = Image.open("photos\\saveimg.jpg")
img = Image.open("photos\\pic.jpg")

# channel operations
overlay = ImageChops.overlay(bear, bird)
dark = ImageChops.darker(bear, bird)
light = ImageChops.lighter(bear, bird)
softl = ImageChops.soft_light(bear, bird)
hardl = ImageChops.hard_light(bear, bird)
diff = ImageChops.difference(bear, bird)
modulo = ImageChops.add_modulo(bear, bird)
screen = ImageChops.screen(bear, bird)

# more complex operations 
add = ImageChops.add(bear, bird, scale=2, offset=0)     # default of scale is 1.0 while offset is 0 
sub = ImageChops.subtract(bear, bird, scale=2, offset=0) 
logic = ImageChops.logical_and(bear.convert("1"), bird.convert("1"))    # image mode should be same so we are converting it into "1" mode, you can convert it into "0" mode also
logic2 = ImageChops.logical_or(bear.convert("1"), bird.convert("1"))     # opposite of logical_and

# extra, for inverting image color
inve = ImageChops.invert(bear)

inve.show()
