# def init make, model, year

class Car:
    wheels = 4

    def __init__(self, owner, make, model, year):
        self.owner = owner
        self.make = make
        self.model = model 
        self.year = year
        
    def __str__(self): 
        return "%s's car is a %d %s %s." % (self.owner, self.year, self.make, self.model)

    def age(self):
        age = 2020 - self.year
        return "%s's %s is %d years old." % (self.owner, self.model, age)

brittani = Car("Brittani", "Subaru", "Legacy", 2015)
maddy = Car("Maddy", "Ford", "Fiesta", 2012)

print(brittani)
print(brittani.age())
print(maddy)