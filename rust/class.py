from dataclasses import dataclass

@dataclass
class Rectangle:
    width: int
    height: int

@dataclass
class ColoredRectangle:
    rectangle: Rectangle
    color: str


# Function to calculate the area of a rectangle
def area(rect: Rectangle) -> int:
    return rect.width * rect.height

def color(rect: ColoredRectangle) -> str:
    return rect.color

# Example usage
rect = Rectangle(10, 20)
colored_rect = ColoredRectangle(rectangle=rect,color="blue")
print("Area of rectangle:", area(rect))
print("Color of rectangle: ", colored_rect.color)