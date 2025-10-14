class Car:
    """A simple attempt to represent a car."""

    def __init__(self,make,model,year):
        """Initialize attributes to describe a car"""

        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        """Return a neatly formated descriptive name"""

        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def odometer_reading(self):
        print(f"this cars odometer is at {self.odometer} miles.")

    def update_odometer(self,mileage):
        self.odometer = mileage

        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You cant roll back odometer!")

    def increment_odometer(self,miles):
        self.odometer+= miles


my_used_car = Car("Subaru ","OUTBACK",2019)

print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.odometer_reading()

my_used_car.increment_odometer(100)

my_used_car.odometer_reading()