"""
As you can see, the code is broken.
Create the missing functions, use default arguments.
Sometimes you have to use 'return' and sometimes you dont.
Start by creating the functions
"""

# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#############################


def is_on_list(days, a):
    return a in days


print("Is Wed on 'days' list?", is_on_list(days, "Wed"))


#############################
def get_x(days, z):
    return days[z]


print("The fourth item in 'days' is:", get_x(days, 3))


#########################################
def add_x(days, x):
    return days.append(x)


add_x(days, "Sat")
print(days)


#########################################
def remove_x(days, y):
    return days.remove(y)


remove_x(days, "Mon")
print(days)

# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #
