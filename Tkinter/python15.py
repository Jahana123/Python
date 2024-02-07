class car:
    def __init__(self,color,size,speed):
        self.color=color
        self.size=size
        self.speed=speed
    def drive(self):
        print(f"The{self.color} car is driving at {self.speed} mph.")
    def stop(self):
        print(f"The {self.color} car has stopped.")
    def honk(self):
        print(f"The {self.color} car is honking.")
red_car=car("red","medium",60)
blue_car=car("blue","small",40)
green_car=car("green","large",80)
print(f"The {red_car.color} car is {red_car.size} in size and has a speed of {red_car.speed} mph.")
print(f"The {blue_car.color} car is {blue_car.size} in size and has a speed of {blue_car.speed} mph.")
print(f"The {green_car.color} car is {green_car.size} in size and has a speed of {green_car.speed} mph.")
red_car.drive()
blue_car.stop()
green_car.honk()
