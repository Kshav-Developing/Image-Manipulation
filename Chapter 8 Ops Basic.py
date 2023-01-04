from PIL import Image, ImageOps

image = Image.open("photos\\pic.jpg")

# Image ops is used for many things like mirroring and works like a filter


# Color Changes 
image_cont = ImageOps.autocontrast(image)       # autocontrast - smarter way to use contrast
image_inv = ImageOps.invert(image)              # invert - inverts the color
image_sol = ImageOps.solarize(image, 100)       # solarize - inverts the image if given less value
image_po = ImageOps.posterize(image, 2)         # posetrize - reduces the amount of colors used  
image_gray = ImageOps.grayscale(image)          # grayscale - uses only black and white colors to fill the image
image_equa = ImageOps.equalize(image)           # equalize
image_colo = ImageOps.colorize(image = image.convert("L"), black = "green", white = "blue")     # black and white are just variables but "L" (Luminosity) mode should be used to change the colors


# Dimension changes
image_mir = ImageOps.mirror(image)                   # mirror - easily flips the image horizontally
image_flip = ImageOps.flip(image)                    # flips - easily flips the image vertically
image_scale = ImageOps.scale(image, 0.1)             # scale - makes the image bigger or smaller based on the integer passed (used only small integers)
image_contain = ImageOps.contain(image, (500,200))   # contain - resizes the image but doesn't change the aspect ratio        

# Element changes 
image_bord = ImageOps.expand(image, 100, "blue")     # expand - creates a border around the image provided with the border width and the border color
image_pad = ImageOps.pad(image, (1000, 1000))        # pad - little same as border but makes the image smaller so that there is a gap between the borders and the image
image_fit = ImageOps.fit(image, (300,300))           # fit - fixes the image to a certain size mentioned
image_crop = ImageOps.crop(image, 500)                # crop - crops the image to the border number

image_crop.show()