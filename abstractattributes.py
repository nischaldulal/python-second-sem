from abc import ABC, abstractmethod

class Shape(ABC):
    
    @property
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass
    
    @property
    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass

# Concrete subclass implementing the abstract attributes
class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def area(self):
        return self.width * self.height
    
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

# Creating an instance of the concrete class
rectangle = Rectangle(5, 10)
print(f"Area: {rectangle.area}")        # Output: Area: 50
print(f"Perimeter: {rectangle.perimeter}")  # Output: Perimeter: 30
