#1 Create two variables – one with your name and one with your age
my_name = input("What's your name? ")
my_age = input("What's your age? ")

#2 Create a function which prints your data as one string
def my_data():
    """Prints the user name (uses global variables)."""
    print(f'{my_name} {my_age}')

my_data()

#3 Create a function which prints ANY data (two arguments) as one string
def print_concatenated_data(el1, el2):
    """Print two concatenated strings.
    
    Arguments:
        :param el1: The first string to be concatenated.
        :param el2: The second string to be concatenated.
    """
    print(f'{el1} {el2}')

print_concatenated_data(my_name, my_age)

#4 Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)
def calculate_decades(age):
    """Calculates the int part of the age received.
    
    Arguments:
        :param age: The age for which the decades should be calculated.

    Returns the decades lived.
    """
    decades_lived = age // 10
    return(decades_lived)

decades = calculate_decades(int(my_age))
print(decades)