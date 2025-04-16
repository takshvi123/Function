import turtle
import math

def draw_circle_and_calculate_circumference(radius):
    """
    Draws a circle using the turtle module and calculates its circumference.
    """
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Circumference Calculator")
    screen.bgcolor("white")
    
    # Set up the turtle
    pen = turtle.Turtle()
    pen.speed(2)  # Set animation speed
    pen.color("blue")
    pen.pensize(2)
    
    # Draw the circle
    pen.penup()
    pen.goto(0, -radius)  # Position the turtle to start drawing the circle
    pen.pendown()
    pen.circle(radius)

    # Calculate the circumference
    circumference = 2 * math.pi * radius

    # Display radius and circumference
    pen.penup()
    pen.goto(-radius, radius + 10)
    pen.pendown()
    pen.write(f"Radius: {radius}", align="center", font=("Arial", 14, "normal"))
    pen.penup()
    pen.goto(-radius, radius - 20)
    pen.pendown()
    pen.write(f"Circumference: {circumference:.2f}", align="center", font=("Arial", 14, "normal"))

    # Hide the turtle after finishing
    pen.hideturtle()
    screen.mainloop()  # Keep the window open

def main():
    """
    Main function to take user input and display circle circumference.
    """
    print("Welcome to the Circle Circumference Calculator!")
    try:
        # Prompt user for the radius
        radius = float(input("Enter the radius of the circle: "))
        if radius <= 0:
            print("Please enter a positive number for the radius!")
        else:
            draw_circle_and_calculate_circumference(radius)
    except ValueError:
        print("Invalid input! Please enter a numeric value for the radius.")

if __name__ == "__main__":
    main()
