from PIL import Image, ImageOps

# The most complicated part
# Deformer is like cutting out few parts (any shape) from the original image and then creates a new image using the cut out parts from the original image and are quite randomly placed in the new image.
class Deformer : 
    def getmesh(self, img) : 
        w,h = img.size
        # define a shape in the original image 
        sourceshape = (0,0,h,w,w,h,w,0)          # (0,0,0,h,0,w,w,0)
        # define a rectangle in the new image (always rectangle) 
        target_rect = (0,0,100,200)       # left, top, right, bottom
        # return all the shapes
        return[(target_rect, sourceshape)]

image = Image.open("photos\\pic.jpg")
image1 = ImageOps.deform(image, Deformer())

image1.show()