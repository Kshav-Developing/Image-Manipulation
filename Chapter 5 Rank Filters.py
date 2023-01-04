from PIL import Image, ImageFilter

image = Image.open("photos\\pic.jpg")

# use odd arguments only
image_fil_min = image.filter(ImageFilter.MinFilter(11))
image_fil_med = image.filter(ImageFilter.MedianFilter(11))
image_fil_max = image.filter(ImageFilter.MaxFilter(11))


image_fil_med.show()