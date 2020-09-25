"""
methods can be passed something called arguments.
arguments are data that has been passed in to the method.
"""
# passing in predefined arguemtns
def main(num1, num2):
    print(num1 + num2)
    
# passing an array of argumetns
def main2(*argv):
    for arg in argv:
        print(arg)

# passing a dictionary of arguments
def main3(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

if __name__ == "__main__":
    main(1, 2)
    # main2('test1', 'test2')
    # main3(name="name", age = 8)