# variables are jus a container for data.
# you set a variable by nameOfVariable = data
def main():
    name = "name"
    print(name)

"""
you have different data types to hold diffrent data
python unlike C has implict typing meaning it assigns the data type on run time
there are some key words that can't be used as a varible name as pyhton uses them in there interperter for other funtions
and, as, assert, break, class, continue, def, del, elif, else, except, False, finally, for, from, global, if, import, in, is, lambda, None, not, or, pass, raise, return, True, try, while, witch, yield
"""

def DataTypes():
    # primitive data types
    num = 1
    string = "string"
    boolean = True
    floatingPoint = 1.2
    character = 'c'
    # abstract data types
    array = [1,2]
    Tuple = (1,2)
    Dictionary = {"Key":"value"}
    print(num, string, boolean, floatingPoint, character, array, Tuple, Dictionary)




if __name__ == "__main__":
    main()
    # DataTypes()