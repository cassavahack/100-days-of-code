# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")


# Functions wiht more than 1 input

# def greet_with(name = 1,location =2):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")
#
#
#
# greet_with(location = "Cleveland", name= "bob")

# def calculate_love_score(name1,name2):
#     total_number = 0
#     for letter in name1:
#         if letter in "truelove":
#             total_number += 1
#     total_number_2 = 0
#     for letters in name2:
#         if letters in "truelove":
#             total_number_2 += 1
#
#     print(f"{total_number}{total_number_2}")
#
#
# calculate_love_score("Kanye West", "Kim Kardashian")


def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    print(score)


calculate_love_score("Kanye West", "Kim Kardashian")
