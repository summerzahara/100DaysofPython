def add(*args):
    result = 0
    for n in args:
        result += n
    return result


print(add(1, 2, 3, 4, 5))


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Tesla", model="Model 3")
your_car = Car(make="Rivian")
print(my_car.model)
print(your_car.make)
