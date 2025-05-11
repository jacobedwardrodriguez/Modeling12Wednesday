"""
This module defines a ColorPoint class that extends the Point class,
adding color as an attribute and overriding string representation.
Includes example usage for demonstration and testing.
"""

from point import Point
import random

class ColorPoint(Point):
    """
      A Point subclass that includes color information.
      """
    def __init__(self, x, y, color):
         # raise an exception if we try to have not a number

        if not isinstance(x,(int, float)):
            raise TypeError ("x must be a number")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be a number")
        """
            Initialize a ColorPoint instance.

            Args:
                x (int or float): X-coordinate.
                y (int or float): Y-coordinate.
                color (str): A string representing the color of the point.

            Raises:
                TypeError: If x or y is not a number.
            """
        super().__init__(x,y)
        self.color = color


    def __str__(self):
        return f"<{self.color}: {self.x}, {self.y}>"
    """
        Return a string representation including color.

        Returns:
            str: A string in the format '<color: x, y>'.
        """
if __name__ == "__main__":
    p = ColorPoint(1, 2, "red")
    print(p.distance_orig())
    print(p)

# colors = ["red", "green", "blue", "yellow", "black", "magenta", "cyan", "white", "burgundy", "periwinkle", "marsala"]
# color_points = []
# for i in range(10):
#     color_points.append(
#         ColorPoint(random.randint(-10,10),
#                    random.randint(-10, 10),
#                    random.choice(colors)))
#
#     print(color_points)
#     color_points.sort()
#     print(color_points)