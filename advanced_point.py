"""
This module defines an AdvancedPoint class that extends ColorPoint,
adds strict color validation, property-based attribute access, and utility methods
for construction and distance calculation.
"""

from color_point import ColorPoint

class AdvancedPoint(ColorPoint):
    COLORS = ["red", "blue", "green", "yellow", "black", "white", "periwinkle"]
    def __init__ (self, x, y, color):
        """
               Initialize an AdvancedPoint instance with validated color.

               Args:
                   x (float or int): The x-coordinate.
                   y (float or int): The y-coordinate.
                   color (str): A color from the predefined COLORS list.

               Raises:
                   TypeError: If the color is not in the allowed COLORS.
               """
        if color not in self.COLORS:
            raise TypeError(f"Invalid color, must be one of {self.COLORS}")
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x  #getter method
    """Get the x-coordinate."""

    @x.setter
    def x(self, value):
        self._x = value #setter method
    """Get the x-coordinate"""

    @property
    def y(self):
        return self._y
    """Get the y-coordinate."""

    @property
    def color(self):
        return self._color
    """Get the point's color."""

    @classmethod
    def add_color(cls, color):
        """
        Adds a new valid color for our class. Applies to the class as a WHOLE.
        """
        cls.COLORS.append(color)

    @staticmethod
    def from_tuple(coordinate, color = "red"):
        """
        Creates a new point from a tuple rather than 2 individual values
        """
        x, y = coordinate
        return AdvancedPoint(x, y, color)

    @staticmethod
    def distance_2_points(p1, p2):
        return ((p1.x - p2.x)**2 + (p1.y - p2.y) ** 2) ** 0.5
"""
     Compute the Euclidean distance between two points.

        Args:
            p1 (AdvancedPoint): First point.
            p2 (AdvancedPoint): Second point.

        Returns:
            float: The distance between p1 and p2.
        """
    def distance_to_other(self, p):
        return ((self.x - p2.x)**2 + (self.y - p2.y) ** 2) ** 0.5

    """
     Compute distance from this point to another point.

     Args:
         p (AdvancedPoint): The other point.

     Returns:
         float: Distance between self and p.
         """


AdvancedPoint.add_color("rojo")

p = AdvancedPoint(1, 2, "blue")

print(p.x. = 11)

print(p)
print(p.distance_orig())

p2 = AdvancedPoint.from_tuple((3,2))
print(p2)

print(AdvancedPoint.distance_2_points(p, p2))
print(p.distance_to_other(p2))



