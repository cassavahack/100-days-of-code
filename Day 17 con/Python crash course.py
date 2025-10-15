


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self,battery_size = 40):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 40:
            ranges = 150
        elif self.battery_size == 65:
            ranges = 225

        print(f"This car go about {ranges} miles on a full charge.")


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""
    def __init__(self,make,model,year):
        """Initialize attributes of the parent class"""
        super(). __init__(make,model,year)
        self.battery = Battery()



    def fill_gas_tank(self):
        """Electric cars dont have gas tanks"""
        print("This car doesnt have a gas tank!")

my_electric_car = ElectricCar('nissan',"leaf", 2024)
print(my_electric_car.get_descriptive_name())
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()