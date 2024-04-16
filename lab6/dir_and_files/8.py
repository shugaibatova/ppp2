class Object:
    def __init__(self, mass, velocity):
        self.mass = mass
        self.velocity = velocity

def collide(obj1, obj2):
    total_mass = obj1.mass + obj2.mass
    final_velocity_obj1 = ((obj1.mass - obj2.mass) / total_mass) * obj1.velocity
    final_velocity_obj2 = ((2 * obj1.mass) / total_mass) * obj1.velocity

    obj1.velocity = final_velocity_obj1
    obj2.velocity = final_velocity_obj2

# Create two objects
obj_X = Object(10, 5)  # mass = 10, velocity = 5
obj_Y = Object(20, 0)  # mass = 20, velocity = 0

# Before collision
print("Before collision:")
print("Object X velocity:", obj_X.velocity)
print("Object Y velocity:", obj_Y.velocity)

# Collision
collide(obj_X, obj_Y)

# After collision
print("\nAfter collision:")
print("Object X velocity:", obj_X.velocity)
print("Object Y velocity:", obj_Y.velocity)
