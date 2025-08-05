import turtle
import colorsys

# Setup turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)

# Drawing variables
n = 36  # Color steps
h = 0   # Starting hue

# Draw colorful pattern
for i in range(460):
    # Convert HSV to RGB
    r, g, b = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1 / n
    t.color(r, g, b)
    
    t.left(145)
    for j in range(5):
        t.forward(300)
        t.left(150)

# Keep the window open
turtle.done()
