# Duck typing is a core concept in Python that revolves around an object’s behavior rather than its class or type. This means you’re more interested in what an object can do (i.e., the methods it has), rather than what it is (i.e., its class or type). It’s a unique approach that makes Python a highly flexible and dynamic language.
class Car:
    def move_forward(self):
        print("Car is driving forward.")

class Bicycle:
    def move_forward(self):
        print("Bicycle is pedaling forward.")

class Motorcycle:
    pass
    # def move_forward(self):
    #     print("Motorcycle is accelerating forward.")


if __name__ == "__main__":

    def move_anything_forward(obj):
        if hasattr(obj,'move_forward'):
            obj.move_forward()
        else:
            print(f"{obj} has no move_foward method")

    # Creating instances of different classes
    car = Car()
    bicycle = Bicycle()
    motorcycle = Motorcycle()


    # Using the move_anything_forward function with different objects
    move_anything_forward(car)        # Output: Car is driving forward.
    move_anything_forward(bicycle)    # Output: Bicycle is pedaling forward.
    move_anything_forward(motorcycle)# Output: Motorcycle is accelerating forward.
