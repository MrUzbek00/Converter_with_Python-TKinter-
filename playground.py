def add(*arg):
    total = 0
    for n in arg:
        total+=n
    
    return total

print(add(1,2,3,4,5,6,7,8,9,10))



def calculate(**kwargs):
    print(kwargs)
calculate(add = 10, multiply = 5)


#Class with kwargs

class Car:
    def __init__(self, **kw) -> None:
        self.model = kw.get("model") # kw["model"] can be used but if it is not assigned before calling it crashes
        self.make = kw.get("make") # get() method is used so that if the senerio above happend, it returns "None"

my_car = Car(make = "GM", model="Mustang")

print(my_car.model)