# when creating a method it can return nothing or it can return a value like so
# the return value can be any data type you wish including custom class you've made (see Object-oriented-programming file 1)

#main return nothing
def main():
    result = sum(1, 5)
    print(result)

# sum returns a inter or float depening on the arguments passed
def sum(*argv):
    total = 0
    for arg in argv:
        total += arg
    return total


if __name__ == "__main__":
    main()