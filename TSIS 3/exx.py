class Person():
    def __init__(self):
        pass
    def sum(self):
        return 0
        
class Child(Person):
    def __init__(self,k):
        Person.__init__(self)
        self.ko=k
    def sum(self):
        return (self.sum)**2
x=Child()
print(x.sum())
    
