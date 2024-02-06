# Define a class named Rectangle which inherits from Shape class from task 2.
#  Class instance can be constructed by a length and width. 
# The Rectangle class has a method which can compute the area.
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self,l,w):
        Shape.__init__(self)
        self.length=l
        self.width=w
    def area(self):
        return self.length*self.width
x=Rectangle(5,6) #input l and w here ~ now l=5, w=6
print(x.area())