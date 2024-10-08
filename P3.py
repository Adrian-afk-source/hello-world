import math

def calculate_circle_area(radius):
    """Calculates the area of a circle given its radius."""
    return math.pi * radius**2

if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))
    radius = calculate_circle_area(radius)
    print(f"The area of the circle is: {area:.2f}")
