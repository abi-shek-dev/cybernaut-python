import turtle
import random

# --- Setup the Turtle Screen ---
# Create a screen object
screen = turtle.Screen()
screen.title("Realistic Rose Drawing")
screen.bgcolor("#1a1a1a") # Dark background color
screen.tracer(0) # Turn off screen updates for instant drawing

# --- Create the Turtle ---
rose_turtle = turtle.Turtle()
rose_turtle.speed(0) # Set the drawing speed to the fastest
rose_turtle.hideturtle() # Hide the turtle icon

def draw_realistic_petal(t, radius, angle, color, raggedness=0.2):
    """
    Draws a more realistic and imperfect petal.
    - t: The turtle object.
    - radius: The base radius of the petal.
    - angle: The base angle for the petal's curve.
    - color: The color of the petal.
    - raggedness: How much imperfection to add to the petal edge.
    """
    t.color(color)
    t.begin_fill()
    
    # Draw one side of the petal with imperfections
    for _ in range(int(angle / 10)):
        # Introduce slight variations in the arc
        rad_variance = radius * random.uniform(-raggedness, raggedness)
        ang_variance = angle * random.uniform(-raggedness/2, raggedness/2)
        t.circle(radius + rad_variance, 10 + ang_variance)

    t.left(180 - angle)

    # Draw the other side of the petal with imperfections
    for _ in range(int(angle / 10)):
        rad_variance = radius * random.uniform(-raggedness, raggedness)
        ang_variance = angle * random.uniform(-raggedness/2, raggedness/2)
        t.circle(radius + rad_variance, 10 + ang_variance)
        
    t.left(180 - angle)
    t.end_fill()

def draw_rose():
    """
    Draws the complete rose by layering petals with random variations.
    """
    # --- Center of the Rose (Tightly Coiled) ---
    rose_turtle.penup()
    rose_turtle.goto(0, 0)
    rose_turtle.pendown()
    
    num_center_petals = 20
    center_radius = 25
    # Expanded color palette for smoother gradients
    center_colors = ["#f2f2f2", "#e6e6e6", "#d9d9d9", "#cccccc", "#bfbfbf"]

    for i in range(num_center_petals):
        # Vary the radius and angle slightly for a more organic look
        r = center_radius - i * 1.1
        a = 90 + i * 4 + random.uniform(-10, 10)
        color = random.choice(center_colors)
        draw_realistic_petal(rose_turtle, r, a, color, 0.1)
        rose_turtle.left(360 / num_center_petals + random.uniform(-5, 5))

    # --- Middle Layer of Petals ---
    num_middle_petals = 15
    middle_radius = 90
    middle_colors = ["#bfbfbf", "#b3b3b3", "#a6a6a6", "#999999"]

    for i in range(num_middle_petals):
        # Position the turtle for the next layer with randomness
        rose_turtle.penup()
        rose_turtle.goto(0,0)
        rose_turtle.setheading(0)
        # Add random offset to rotation and distance
        rose_turtle.left(i * (360 / num_middle_petals) + random.uniform(-10, 10))
        rose_turtle.forward(random.uniform(15, 25))
        rose_turtle.pendown()

        color = random.choice(middle_colors)
        draw_realistic_petal(rose_turtle, middle_radius, 75, color, 0.2)

    # --- Outer Layer of Petals ---
    num_outer_petals = 12
    outer_radius = 160
    outer_colors = ["#8c8c8c", "#808080", "#737373", "#666666"]

    for i in range(num_outer_petals):
        # Position the turtle for the final layer with more randomness
        rose_turtle.penup()
        rose_turtle.goto(0,0)
        rose_turtle.setheading(0)
        # Add significant random offset for a more natural, layered look
        rose_turtle.left(i * (360 / num_outer_petals) + random.uniform(-20, 20))
        rose_turtle.forward(random.uniform(40, 60))
        rose_turtle.pendown()

        color = random.choice(outer_colors)
        # Use a higher raggedness for the outer, more weathered petals
        draw_realistic_petal(rose_turtle, outer_radius, 60, color, 0.3)


# --- Main Execution ---
if __name__ == "__main__":
    draw_rose()
    screen.update() # Update the screen to show the final drawing
    turtle.done() # Keep the window open
