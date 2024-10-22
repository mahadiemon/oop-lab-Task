# Base Shape class
class Shape:
    def __init__(self, name):
        self._name = name  # Protected attribute

    # Private method to display shape type
    def __display_shape_type(self):
        print(f"This is a shape of type: {self._name}")

    # Public method to display shape type using the private method
    def show_shape_type(self):
        self.__display_shape_type()

# Rectangle class, inheriting from Shape
class Rectangle(Shape):
    def __init__(self, name, length, width):
       ## super().__init__(name)
        self.__length = length  
        self.__width = width    

    # Getter method for length
    def get_length(self):
        return self.__length

    # Getter method for width
    def get_width(self):
        return self.__width

# Example usage:
shape = Shape("Generic Shape")
shape.show_shape_type()

rect = Rectangle("Rectangle", 10, 5)
rect.show_shape_type()
print("Length:", rect.get_length())
print("Width:", rect.get_width())
