#  To iterate over a set number you can use a for loop using range like range(start, stop, step)
def BasicForLoop():
    for i in range(0, 5, 1):
        print(i)

# To iterate over a array or set of items you can use the for loop like this where letter is eqivalent to array[index]
def BasicForEachLoop():
    array = ["a","b","c","d","e","f","g"]
    for letter in array:
        print(letter)

# The while loop keeps looping till the condition set is met so as long as num is less than 5 it will loop in this case.
# With while loops you have to be careful of getting stuck in a infinate loop where the condition is never met. 
def WhileLoop():
    num = 0
    while num < 5:
        print(num)
        num += 1

if __name__ == "__main__":
    BasicForLoop()
    # BasicForEachLoop()
    # WhileLoop()