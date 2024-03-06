class Person:
    def __init__(self):
        pass
    def sum(self):
        return 0       
class Child(Person):
    def __init__(self,k):
        Person.__init__(self)
        self.ko=k
    def sum(self):
        return (self.ko)**2
x=Child(4)
print(x.sum())
    