# Write the definition of a Point class. Objects from this class should have a

# 1 a method show to display the coordinates of the point
# 2 a method move to change these coordinates
# 3 a method dist that computes the distance between 2 points
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, new_point):
        dx = self.x - new_point.x
        dy = self.y - new_point.y
        distance = (dx*dx + dy*dy)**0.5
        return distance

point1 = Point(1, 2) #input coordinates of 1-point  here/ now 1-point(1,2)
point2 = Point(3, 4) #input coordinates of 2-point  here/ now 2-point(3,4)

point1.show()  
point2.show()  

point1.move(6, 8) #change coordinates of 1-point here/ now new 1-point(5,6)
point1.show()  

distance = point1.dist(point2)
print(f"Distance between point1 and point2: {distance}")
