"""
Importing in very important though out most coding lanuages, it allows you to use prewritten code from yourself or over people.
when importing someone else code you will have use the pip install command in cmd (for windows) or terminal (for Mac) to first get the package
off the internet. 
if your importing your own code just make sure it's in the same folder as the file your importing it to. 
"""

# we're going to import numpy and matplotlib as they are commanly used for any math and data displaying.
# numpy --> pip install numpy (normally already installed just making sure)
# matplotlib --> pip install matplotlib


def main():  
    import numpy as np # import entier libary 
    # working with matrixs
    a = np.matrix([[1,2],[3,4]])
    b = np.matrix([[1,0],[0,1]])
    print(a * b) # should be the same a variable a as b is the identity matrix

def main2():
    # basic linear line
    import matplotlib.pyplot as plt 
    plt.plot([1,2,3,4,5,6,7,8,9,10])
    plt.show()

def main3():
    # postive half of a quadratic
    import matplotlib.pyplot as plt 
    plt.plot([1,2,3,4], [1,4,9,16])
    plt.show()



if __name__ == "__main__":
    # main()
    # main2()
    main3()