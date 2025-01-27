class Device:
    
   # A base class representing a general device.
 
    def __init__(self, brand, model):
        self.__brand = brand  
        self.__model = model  

    def device_info(self):
        return f"Brand: {self.__brand}, Model: {self.__model}"

    # Getter for brand
    def brand(self):
        return self.__brand

    # Setter for brand
    def brand(self, new_brand):
        self.__brand = new_brand


class Smartphone(Device):
   
   # Derived class representing a Smartphone.
 
    def __init__(self, brand, model, storage, battery_life):
        super().__init__(brand, model)
        self.storage = storage  
        self.battery_life = battery_life  
    def smartphone_info(self):
        return (
            f"{self.device_info()}, Storage: {self.storage}GB, Battery Life: {self.battery_life} hours"
        )

    def use_battery(self, hours):
        
      #use the phone for a number of hours.
        
      if hours <= self.battery_life:
          self.battery_life -= hours
          return f"Used for {hours} hours. Battery remaining: {self.battery_life} hours."
      else:
          return "Battery not sufficient for that duration."


class GamingSmartphone(Smartphone):
    
  #Derived class that represents a Gaming Smartphone.
    
  def __init__(self, brand, model, storage, battery_life, cooling_system):
      super().__init__(brand, model, storage, battery_life)
      self.cooling_system = cooling_system  

  def gaming_info(self):
      return f"{self.smartphone_info()}, Cooling System: {self.cooling_system}"

  def play_game(self, hours):
      if hours <= self.battery_life:
          self.battery_life -= hours
          return f"Played games for {hours} hours. Battery remaining: {self.battery_life} hours."
      else:
          return "Not enough battery for gaming."


