from math import hypot

class Vector:
    """
    This is a python implementation of a vector that supports meta programming for
    * addition
    * multiplication
    * absolute
     and representation
    """
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)
    
    def __mul__(self, value):
        return Vector(self.x * value, self.y * value)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
if __name__ == "__main__":
    my_vector = Vector(1, 2)
    other_vector = Vector(3, 4)
    
    print("My first vector is : ", my_vector)
    print("My second vector is : ", other_vector)
    
    print("The addition of the two vectors is : ", my_vector + other_vector)
    print("Multiplying vector 2 by 3 results in : ", other_vector * 3)
    print("The absolute value of vector 1 is : ", abs(my_vector))
    print("The boolean value for vector 2 is : ", bool(other_vector))