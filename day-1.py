#functions to perform the following maths operations
def addTwovalues(value_one,value_two):
    return value_one + value_two

def multiplyvalues(value_three,value_four):
    return value_three * value_four

def dividevalues(value_five,value_six):
   return value_five / value_six

def substractvalues(value_seven,value_eight):
    return value_seven - value_eight

# Input two numbers
a = int(input("\nFirst number :"))
b = int(input("\nSecond number :"))

# Display outputs after operations
print(addTwovalues(a,b))
print(multiplyvalues(a,b))
print(dividevalues(a,b))
print(substractvalues(a,b))
