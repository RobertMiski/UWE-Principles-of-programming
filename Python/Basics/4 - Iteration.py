#  To iterate over a set number you can use a for loop using range like range(start, stop, step)
def BasicForLoop():
    for i in range(0, 5, 1):
        print(i)

# To iterate over a array or set of items you can use the for loop like this where letter is eqivalent to array[index]
def BasicForEachLoop():
    array = ["a","b","c","d","e","f","g"]
    for letter in array:
        print(letter)
# To iterate through a dictionary you have many ways here is one where you get both the keys and values of each item.
def BasicDictionaryLoop():
    dic = {"name":"name", "age": 20}
    for key, value in dic.items():
        print("{0} = {1}".format(key, value))
# Basic string loop to access each charatcer in the string you can also use for i in range(0 string.length, 1): string[i] 
def stringLoop():
    string = "test string"
    for char in string:
        print(char)

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
    # BasicDictionaryLoop()
    # WhileLoop()
    # stringLoop()