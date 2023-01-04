from PIL import Image, ImageDraw, ImageFont   # Importing ImageDraw


image = Image.open("photos\\pic.jpg")
draw = ImageDraw.Draw(image)

# drawing shapes
draw.rectangle((0, 0, 700, 500), fill="red", outline="black", width=10)
draw.ellipse((0,0,700,500), fill="blue", outline="yellow", width=20)

# drawing circles
draw.arc((800,100,1000, 200), start=30, end=180, fill="white", width=20)        # start, end refers to the angle the PIL should start from and end it.
draw.chord((800,100,1000, 400), start=30, end=180, fill="white", width=20) 
draw.pieslice((1000,300,2000, 800), start=30, end=180, fill="white", width=20)      # creates a pie chart type thing

# drawing texts 
font = ImageFont.truetype("arial.ttf", 50)
draw.text((900,1200), text="Text is here", font = font, fill = "cyan")

image.show()