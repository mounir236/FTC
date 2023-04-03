valid = False

try:
    f_temp = float(input("What is the temperature in degrees farenheit?"))
    valid = True
except:
    print("That's not a valid option!")


if valid == True:
    f_temp = (f_temp - 32) * (5 / 9)

    print(f"The temperature is {f_temp} degrees celcius.")