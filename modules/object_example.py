class Animal(object):
           def __init__(self, animal_name):
                  self.IsAlive = True
                  self.name = animal_name
           def breathe(self, breath_per_minute):
                  print("DEEP BREATH")
 
class Bird(Animal):
    def __init__(self, color, animal_name):
        self.feathers = color
        super().__init__(self, animal_name)
    def fly(self):
        print(self.name, "is flying!")


anim1=Animal("Josh")
anim1.IsAlive
anim1.name
anim1.breathe(5)
bird1 = Bird("red", animal_name="Mike")
print(bird1.IsAlive)
print(bird1.name)
print(bird1.fly())
print(bird1.feathers)

# can't make this work. Why?