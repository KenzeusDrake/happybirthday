import turtle
import random

# Set up the screen with dimensions to ensure everything is visible
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("HAPPY BIRTHDAY")
screen.setup(width=1200, height=700)

# Create the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.pensize(8)
t.color("#39FF14")  # Bright neon green

# Function to create a star
def draw_star(t, x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

# Function to create firework
def draw_firework(t, x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.pensize(2)
    
    for _ in range(20):  # 20 lines radiating out
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.setheading(random.randint(0, 360))
        t.forward(size)
        
        # Optional: add small dots at the end of each line
        if random.choice([True, False]):
            t.penup()
            t.forward(5)
            t.pendown()
            t.dot(3)

# Function to create sparkle
def draw_sparkle(t, x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.pensize(1)
    
    # Draw a simple 4-pointed sparkle
    for angle in [0, 90, 45, 135]:
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.setheading(angle)
        t.forward(size)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.setheading(angle + 180)
        t.forward(size)

# Define some festive colors
festive_colors = ["#FF69B4", "#FFD700", "#FF6347", "#00FFFF", "#9370DB", "#FF4500"]

# letter dimensions
height = 90
width = 45
spacing = 22

# Calculate total width
letters = 13
total_width = letters * width + (letters - 1) * spacing
start_x = -total_width / 2
center_y = 200  # Position for text - moved up a bit
start_y = center_y - height/2

# Draw "HAPPY BIRTHDAY"
current_x = start_x

# H
t.penup()
t.goto(current_x, start_y)
t.pendown()
t.setheading(90)
t.forward(height)
t.penup()
t.goto(current_x, start_y + height/2)
t.pendown()
t.setheading(0)
t.forward(width)
t.penup()
t.goto(current_x + width, start_y)
t.pendown()
t.setheading(90)
t.forward(height)
current_x += width + spacing

# A
t.penup()
t.goto(current_x, start_y)
t.pendown()
t.setheading(75)
t.forward(height/0.95)
t.setheading(-75)
t.forward(height/0.95)
t.penup()
t.goto(current_x + width/4, start_y + height/2)
t.pendown()
t.setheading(0)
t.forward(width/2)
current_x += width + spacing

# P
t.penup()
t.goto(current_x, start_y)
t.pendown()
t.setheading(90)
t.forward(height)
t.right(90)
t.forward(width*0.8)
t.right(90)
t.forward(height/2)
t.right(90)
t.forward(width*0.8)
current_x += width + spacing

# P (second P)
t.penup()
t.goto(current_x, start_y)
t.pendown()
t.setheading(90)
t.forward(height)
t.right(90)
t.forward(width*0.8)
t.right(90)
t.forward(height/2)
t.right(90)
t.forward(width*0.8)
current_x += width + spacing

# Y - COMPLETELY REDONE
t.penup()
t.goto(current_x, start_y + height)  # Top left corner
t.pendown()
# Draw left arm
t.goto(current_x + width/2, start_y + height/2)  # Center point
# Draw right arm
t.penup()
t.goto(current_x + width, start_y + height)  # Top right corner
t.pendown()
t.goto(current_x + width/2, start_y + height/2)  # Center point
# Draw stem
t.goto(current_x + width/2, start_y)  # Bottom center
current_x += width + spacing

# Space
current_x += width/2

# B - COMPLETELY REDONE
t.penup()
t.goto(current_x, start_y)  # Bottom left
t.pendown()
# Vertical line
t.goto(current_x, start_y + height)  # Top left
# Top loop
t.goto(current_x + width*0.8, start_y + height)  # Top right
t.goto(current_x + width*0.8, start_y + height*0.6)  # Middle right top
t.goto(current_x, start_y + height*0.5)  # Middle left
# Bottom loop
t.goto(current_x + width*0.8, start_y + height*0.4)  # Middle right bottom
t.goto(current_x + width*0.8, start_y)  # Bottom right
t.goto(current_x, start_y)  # Back to bottom left
current_x += width + spacing

# I
t.penup()
t.goto(current_x, start_y)
t.pendown()
t.setheading(0)
t.forward(width)
t.penup()
t.goto(current_x + width/2, start_y)
t.pendown()
t.setheading(90)
t.forward(height)
t.penup()
t.goto(current_x, start_y + height)
t.pendown()
t.setheading(0)
t.forward(width)
current_x += width + spacing

# R - COMPLETELY REDONE
t.penup()
t.goto(current_x, start_y)  # Bottom left
t.pendown()
# Vertical line
t.goto(current_x, start_y + height)  # Top left
# Top loop
t.goto(current_x + width*0.8, start_y + height)  # Top right
t.goto(current_x + width*0.8, start_y + height*0.5)  # Middle right
t.goto(current_x, start_y + height*0.5)  # Middle left
# Diagonal leg
t.penup()
t.goto(current_x, start_y + height*0.5)  # Middle left again
t.pendown()
t.goto(current_x + width, start_y)  # Bottom right
current_x += width + spacing

# T
t.penup()
t.goto(current_x, start_y + height)
t.pendown()
t.setheading(0)
t.forward(width)
t.penup()
t.goto(current_x + width/2, start_y + height)
t.pendown()
t.setheading(-90)
t.forward(height)
current_x += width + spacing

# H (second H)
t.penup()
t.goto(current_x, start_y)
t.pendown()
t.setheading(90)
t.forward(height)
t.penup()
t.goto(current_x, start_y + height/2)
t.pendown()
t.setheading(0)
t.forward(width)
t.penup()
t.goto(current_x + width, start_y)
t.pendown()
t.setheading(90)
t.forward(height)
current_x += width + spacing

# D - improved
t.penup()
t.goto(current_x, start_y)
t.pendown()
t.setheading(90)
t.forward(height)  # Vertical line
t.right(90)
t.forward(width*0.2)  # Small top line
# Draw the curve of the D
for i in range(180):
    t.right(1)
    t.forward(3.14 * height / 360)
t.forward(width*0.2)  # Small bottom line
current_x += width + spacing

# A (second A)
t.penup()
t.goto(current_x, start_y)
t.pendown()
t.setheading(75)
t.forward(height/0.95)
t.setheading(-75)
t.forward(height/0.95)
t.penup()
t.goto(current_x + width/4, start_y + height/2)
t.pendown()
t.setheading(0)
t.forward(width/2)
current_x += width + spacing

# Y (second Y) - COMPLETELY REDONE
t.penup()
t.goto(current_x, start_y + height)  # Top left corner
t.pendown()
# Draw left arm
t.goto(current_x + width/2, start_y + height/2)  # Center point
# Draw right arm
t.penup()
t.goto(current_x + width, start_y + height)  # Top right corner
t.pendown()
t.goto(current_x + width/2, start_y + height/2)  # Center point
# Draw stem
t.goto(current_x + width/2, start_y)  # Bottom center

# Draw a decorative fancy border - adjusted padding
border_padding = 60
border_x = start_x - border_padding
border_y = start_y - border_padding
border_width = total_width + (2 * border_padding)
border_height = height + (2 * border_padding)

t.penup()
t.goto(border_x, border_y)
t.pendown()
t.pensize(5)

# Draw fancy border with swirls - keeping space between elements
t.color("#FF69B4")  # Hot pink for border
segments = 40
corner_radius = 30

# Bottom side with swirls
for i in range(segments):
    t.forward(border_width / segments)
    if i % 10 == 0 and i > 0 and i < segments-1:  # Even fewer swirls (every 10th segment)
        original_pos = t.position()
        original_heading = t.heading()
        t.pensize(2)
        t.right(90)
        t.forward(10)
        # Draw small spiral
        for _ in range(5):
            t.right(45)
            t.forward(5)
        # Return to original position and heading
        t.penup()
        t.goto(original_pos)
        t.setheading(original_heading)
        t.pendown()
        t.pensize(5)

# Right side curve and straight
t.setheading(90)
for i in range(segments):
    t.forward(border_height / segments)
    if i % 10 == 0 and i > 0 and i < segments-1:
        original_pos = t.position()
        original_heading = t.heading()
        t.pensize(2)
        t.left(90)
        t.forward(10)
        for _ in range(5):
            t.right(45)
            t.forward(5)
        t.penup()
        t.goto(original_pos)
        t.setheading(original_heading)
        t.pendown()
        t.pensize(5)

# Top side with swirls
t.setheading(180)
for i in range(segments):
    t.forward(border_width / segments)
    if i % 10 == 0 and i > 0 and i < segments-1:
        original_pos = t.position()
        original_heading = t.heading()
        t.pensize(2)
        t.left(90)
        t.forward(10)
        for _ in range(5):
            t.right(45)
            t.forward(5)
        t.penup()
        t.goto(original_pos)
        t.setheading(original_heading)
        t.pendown()
        t.pensize(5)

# Left side with swirls
t.setheading(270)
for i in range(segments):
    t.forward(border_height / segments)
    if i % 10 == 0 and i > 0 and i < segments-1:
        original_pos = t.position()
        original_heading = t.heading()
        t.pensize(2)
        t.left(90)
        t.forward(10)
        for _ in range(5):
            t.right(45)
            t.forward(5)
        t.penup()
        t.goto(original_pos)
        t.setheading(original_heading)
        t.pendown()
        t.pensize(5)

# Calculate the center position for message - moved up
message_y = border_y - 70  # Adjusted for better spacing

# Add personalized message - wrapped in multiple lines with safety buffer around them
message_lines = [
    "Hola! Before this day ends, I just want to wish you a Happy Birthday",
    "and thank you for everything. You are truly valued and appreciated,",
    "and your presence makes a difference in so many lives. May you",
    "continue to share the Lord’s wisdom, and know that you are",
    "worth more than words can express. Be blessed, and may",
    "you always be a blessing to those around you!"
]

# Define message safety zone to avoid placing decorations there
message_top = message_y + 20
message_bottom = message_y - (len(message_lines) * 28) - 20  # Reduced line spacing
message_left = -450  # Wide safety zone around message
message_right = 450

# Define function for multi-line text
def draw_multiline_text(lines, y_start, spacing, font_size):
    for i, line in enumerate(lines):
        t.penup()
        t.goto(0, y_start - (i * spacing))
        t.pendown()
        t.write(line, align="center", font=("Arial", font_size, "bold"))

# Draw the message - tighter spacing
t.color("#FFD700")  # Gold color for message
draw_multiline_text(message_lines, message_y, 28, 15)  # Smaller font and spacing

# Add cake decoration - with MUCH more space from message
cake_x = 0
cake_y = message_bottom - 80  # Much more space below message
cake_width = 130  # Slightly smaller cake
cake_height = 50  # Slightly shorter cake

# Define cake safety zone to avoid placing decorations there
cake_top = cake_y + cake_height + 50  # Extra room above for candles
cake_bottom = cake_y - 20
cake_left = cake_x - cake_width/2 - 25
cake_right = cake_x + cake_width/2 + 25

# Draw layered cake
t.penup()
t.goto(cake_x - cake_width/2, cake_y)
t.pendown()

# Bottom layer
t.color("#FF9999")  # Pink
t.begin_fill()
t.setheading(0)
t.forward(cake_width)
t.left(90)
t.forward(cake_height/3)
t.left(90)
t.forward(cake_width)
t.left(90)
t.forward(cake_height/3)
t.end_fill()

# Middle layer
t.penup()
t.goto(cake_x - cake_width*0.8/2, cake_y + cake_height/3)
t.pendown()
t.color("#FFCC99")  # Light orange
t.begin_fill()
t.setheading(0)
t.forward(cake_width*0.8)
t.left(90)
t.forward(cake_height/3)
t.left(90)
t.forward(cake_width*0.8)
t.left(90)
t.forward(cake_height/3)
t.end_fill()

# Top layer
t.penup()
t.goto(cake_x - cake_width*0.6/2, cake_y + cake_height*2/3)
t.pendown()
t.color("#99CCFF")  # Light blue
t.begin_fill()
t.setheading(0)
t.forward(cake_width*0.6)
t.left(90)
t.forward(cake_height/3)
t.left(90)
t.forward(cake_width*0.6)
t.left(90)
t.forward(cake_height/3)
t.end_fill()

# Draw icing
t.penup()
t.goto(cake_x - cake_width/2, cake_y + cake_height/3)
t.color("white")
t.pensize(3)
t.pendown()
for i in range(int(cake_width/10)):
    t.setheading(-90)
    t.forward(5)
    t.backward(5)
    t.setheading(0)
    t.forward(10)

t.penup()
t.goto(cake_x - cake_width*0.8/2, cake_y + cake_height*2/3)
t.pendown()
for i in range(int(cake_width*0.8/10)):
    t.setheading(-90)
    t.forward(5)
    t.backward(5)
    t.setheading(0)
    t.forward(10)

# Draw candles - with extra space and shorter candles
candle_spacing = cake_width*0.6 / 8
candle_x = cake_x - cake_width*0.6/2 + candle_spacing
candle_height = 25  # Shorter candles

for i in range(7):
    # Vary candle colors
    t.penup()
    t.goto(candle_x, cake_y + cake_height)
    t.pendown()
    t.color(random.choice(festive_colors))
    t.pensize(3)
    t.setheading(90)
    t.forward(candle_height)
    
    # Draw flame - smaller flame
    t.color("orange")
    t.begin_fill()
    t.circle(3)  # Smaller flame
    t.end_fill()
    
    # Add minimal glow effect
    t.penup()
    t.goto(candle_x, cake_y + cake_height + candle_height + 4)
    t.pendown()
    t.color("yellow")
    t.pensize(1)
    for _ in range(2):  # Minimal rays
        current_pos = t.position()
        t.setheading(random.randint(0, 360))
        t.forward(3)  # Very short rays
        t.penup()
        t.goto(current_pos)
        t.pendown()
    
    candle_x += candle_spacing

# Check if a point is in any of the safety zones (to avoid overlapping)
def is_in_safety_zone(x, y):
    # Check message zone
    if message_left <= x <= message_right and message_bottom <= y <= message_top:
        return True
    # Check cake zone
    if cake_left <= x <= cake_right and cake_bottom <= y <= cake_top:
        return True
    # Check border zone with small buffer
    buffer = 15
    if (border_x-buffer <= x <= border_x+buffer or 
        border_x+border_width-buffer <= x <= border_x+border_width+buffer or 
        border_y-buffer <= y <= border_y+buffer or 
        border_y+border_height-buffer <= y <= border_y+border_height+buffer):
        return True
    return False

# Define smaller zones that are safely away from all content
safe_star_zones = [
    [-450, -350, 250, 350],  # Left top area
    [350, 450, 250, 350],    # Right top area
    [-450, -350, -300, -200], # Left bottom area
    [350, 450, -300, -200],   # Right bottom area
]

# More stars in safe zones
for zone in safe_star_zones:
    attempts = 0
    stars_added = 0
    while stars_added < 3 and attempts < 20:
        attempts += 1
        x = random.randint(int(zone[0]), int(zone[1]))
        y = random.randint(int(zone[2]), int(zone[3]))
        
        # Only place star if outside safety zones
        if not is_in_safety_zone(x, y):
            size = random.randint(6, 9)
            draw_star(t, x, y, size, random.choice(festive_colors))
            stars_added += 1

# Add fireworks in specific zones
firework_zones = [
    [-450, -350, 300, 350],  # Far left
    [350, 450, 300, 350],    # Far right
]

# Few fireworks to avoid clutter
for zone in firework_zones:
    attempts = 0
    fireworks_added = 0
    while fireworks_added < 1 and attempts < 10:
        attempts += 1
        x = random.randint(zone[0], zone[1])
        y = random.randint(zone[2], zone[3])
        
        # Only place firework if outside safety zones
        if not is_in_safety_zone(x, y):
            size = random.randint(9, 14)
            draw_firework(t, x, y, size, random.choice(festive_colors))
            fireworks_added += 1

# Add sparkles only in very safe areas
sparkle_zones = [
    [start_x - 30, start_x - 15, start_y + height + 15, start_y + height + 30],  # Above left of text
    [start_x + total_width + 15, start_x + total_width + 30, start_y + height + 15, start_y + height + 30],  # Above right of text
]

# Add sparkles
for zone in sparkle_zones:
    for _ in range(2):
        x = random.randint(int(zone[0]), int(zone[1]))
        y = random.randint(int(zone[2]), int(zone[3]))
        if not is_in_safety_zone(x, y):
            size = random.randint(4, 6)
            draw_sparkle(t, x, y, size, "#FFD700")  # Gold sparkles

# Add limited confetti in clear spaces - only far from any content
confetti_zones = [
    [-450, -350, 0, 100],     # Left middle
    [350, 450, 0, 100],       # Right middle
]

# Sparse confetti to avoid clutter
for zone in confetti_zones:
    attempts = 0
    confetti_added = 0
    while confetti_added < 6 and attempts < 20:
        attempts += 1
        x = random.randint(int(zone[0]), int(zone[1]))
        y = random.randint(int(zone[2]), int(zone[3]))
        
        # Only place confetti if outside safety zones
        if not is_in_safety_zone(x, y):
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.dot(random.randint(2, 3), random.choice(festive_colors))
            confetti_added += 1

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()