# Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. 
# The following formula is used for the conversion: C = (5 / 9) * (F – 32)
def  Celsius(temperature):
    celsius=(5/9)*(temperature-32)
    return celsius
print(Celsius(76))
