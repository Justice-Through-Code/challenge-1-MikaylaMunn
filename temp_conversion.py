
def convert_100_to_celsius(f):
    # Convert a temperature of 100 degrees fahrenheit to celsius
    clesius_100 = (f - 32) * 5/9
    # Save this to a variable called celsius_100, and use print() to print out the value
    print(float(clesius_100))
    # Is the resulting temperature you get an integer or float?
        # float
    # Print 'float' if it is a float or 'int' if it is an int
    # How do you know? Write a comment below your code explaining how you know which it is
        #because it is a real number written in a decimal point, where as an integer is a whole number.
convert_100_to_celsius(100)

def convert_0_to_celsius(f):
    # Convert a temperature of 0 degrees fahrenheit to celsius
    # Save this to a variable called celsius_0, and use print() to print out the value
    celsius_0 = (f - 32) * 5/9
    print(celsius_0)
convert_0_to_celsius(0)

def convert_34_2_to_celsius(f):
    # Convert a temperature of 34.2 degrees fahrenheit to celsius
    # Do this one all in one print statement without saving any variables
    print(float( (f - 32) * 5/9))
convert_34_2_to_celsius(34.2)
# '''
#  Now, can you convert back?
# '''

def convert_5_to_fahrenheit(c):
    # Convert a temperature of 5 degrees celsius to fahrenheit and print it out
    fahrenheit_1 = (c *9/5) + 32
    print(fahrenheit_1)
convert_5_to_fahrenheit(5)


def hotter_temp(c):
    # What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
    celsius_1 = (c *9/5) + 32
    fahrenheit_1 = 85.1
    if fahrenheit_1 > celsius_1:
        print('85.1 degrees fahrenheit is hotter')
    else:
        print( '30.2 degrees celsius is hotter')
    # Print out the hotter temp: '30.2 degrees celsius' or '85.1 degrees fahrenheit', respectively.
hotter_temp(30.2)