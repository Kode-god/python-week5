class Vehicle:
  def move(self):
      raise NotImplementedError("This method should be overridden in derived classes.")


class Car(Vehicle):
  def move(self):
     return "Driving "


class Plane(Vehicle): 
  def move(self):
    return "Flying "


class Boat(Vehicle):
  def move(self):
      return "Sailing "


class Train(Vehicle):  
  def move(self):
      return "Chugging along the tracks "


class Bicycle(Vehicle):
  def move(self):
      return "Pedaling "


# demonstrate polymorphism with this function
def demonstrate_movement(vehicles):
    for vehicle in vehicles:
        print(f"{vehicle.__class__.__name__}: {vehicle.move()}")


# instances of each vehicle
car = Car()
plane = Plane()
boat = Boat()
train = Train()
bicycle = Bicycle()

# testing polymorphism
vehicles = [car, plane, boat, train, bicycle]
demonstrate_movement(vehicles)
