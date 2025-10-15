class Restaurant:
    """A simple attempt to model a real restaurant"""

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(f"the restaurants name is {self.restaurant_name} and they sell {self.cuisine_type}  ")

    def open_restaurant(self):
        print("The restaurant is open")

    def set_number_served(self,number_of_customers):
        self.number_served = number_of_customers

    def increment_number_served(self,number_of_customers):
        self.number_served += number_of_customers





# my_rest = Restaurant("Pacific East", "Chinese")
#
# print(my_rest.restaurant_name)
# print(my_rest.cuisine_type)
#
# my_rest.open_restaurant()
# my_rest.describe_restaurant()


# rest_1 = Restaurant("Mcdonalds", "Burgers")
#
# rest_2 = Restaurant("Wendy's", "frosties")
#
# rest_3 = Restaurant("Burger king", "crappy fast food")

# rest_1.describe_restaurant()
# rest_2.describe_restaurant()
# rest_3.describe_restaurant()


# restaurant = Restaurant("Pacific East", "Chinese")

# print(restaurant.number_served)
#
# restaurant.number_served = 2
#
# print(restaurant.number_served)


# restaurant.set_number_served(5)
# restaurant.increment_number_served(100)
#
# print(restaurant.number_served)


class IceCreamStand(Restaurant):
    """rREPRESENT ASPECTS OF RESTAURANT SPECIFIC TO ICECREAM STAND"""

    def __init__(self,restaurant_name,cuisine_type,number_served = 0):
        super(). __init__(restaurant_name,cuisine_type)
        self.flavors = ["Vanilla", "chocolate", "peach"]


    def show_flavors(self):
        print(f"we have {self.flavors} for sale")


my_ice_cream_stand = IceCreamStand("The wave","Dessert")

my_ice_cream_stand.show_flavors()