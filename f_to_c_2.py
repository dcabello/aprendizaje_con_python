print("Fahrenheit -> Celsius")
print("----------    -------")
for f in range(-10, 101, 5):
    c = (f - 32) * (100/(212-32))
    print(" {:6.0f}".format(f).ljust(13), " {:6.2f}".format(c))