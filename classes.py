#Classes (don't forget defs)
class Point():
    x: int
    y: int
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def print_x(self):
        print(self.x)

    def print_y(self):
        print(self.y)

me = Point(1, 2)

#me.z = 3 # This will add a new attribute to the object

#me.print_z() # This will throw an error because the object doesn't have a print_z method

#Lambda functions (anonymous functions)
add = lambda x, y: x + y
add(5, 7) # prints 12