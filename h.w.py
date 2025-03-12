def calculate_circumference(radius):
    """
    This function calculates the circumference of a circle.
    :param radius: The radius of the circle
    :return: The circumference of the circle
    """
    if radius < 0:
        return "Radius cannot be negative."
    circumference = 2 * 3.14159 * radius
    return circumference

# Example usage:
radius = float(input("Enter the radius of the circle: "))
print("Circumference of the circle:", calculate_circumference(radius))
