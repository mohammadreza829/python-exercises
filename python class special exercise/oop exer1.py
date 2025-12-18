class Square:
    def __init__(self, side):
        self.side = side
    def calculate_area(self):
        return self.side * self.side
    
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius * self.radius
    

        