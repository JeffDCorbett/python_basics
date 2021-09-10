
def convert_cel_to_far(c):
    f = (c * 9/5) + 32
    return f


def convert_far_to_cel(f):
    c = (f - 32) * 5/9
    return c


user_cel_input = input("Enter Celsius to convert: ")
temperature = convert_cel_to_far(float(user_cel_input))
print(f"The temperature in F is {temperature}")


user_far_input = input("Enter Fahrenheit to convert: ")
temperature = convert_far_to_cel(float(user_far_input))
print(f"The temperature in F is {temperature}")
