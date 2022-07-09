from vehicle import Vehicle


class Car(Vehicle):

    def brag(self):
        print('Look how cool my car is.')


car1 = Car()
car1.drive()
# print(car1.__warnings) warnings method is private and can't be accessed outside the class.
print(car1.get_warnings())

# Car.top_speed = 200
car1.add_warning('New warning!')
# print(car1.__dict__)
print(car1)

car2 = Car(200)
car2.drive()
# print(car2.__warnings) warnings method is private
print(car2.get_warnings())

car3 = Car(250)
car3.drive()
# print(car3.__warnings) warnings method is private
print(car3.get_warnings())
