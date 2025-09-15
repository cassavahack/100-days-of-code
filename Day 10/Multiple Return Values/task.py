# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#     print("fjkdlfkjsdlfkjsdlkfjslkdjf")
#
#
#
# print(format_name("AnGEla", "YU"))


def is_leap_year(year):
    div4 = year % 4
    if div4 != 0:
        print(False)
    elif div4 ==0:
        div100 = year % 100
        if div100 !=0:
            print(True)

        elif div100 == 0:
            div100 = year % 400
            if div100 == 0:
                print(True)
            elif div100 !=0:
                print(False)






is_leap_year(2017)