from pythonds.basic.stack import Stack

def decToBin(decNumber, base):

    stack = Stack()
    digits = "0123456789ABCDEF"

    while decNumber > 0:
        rem = decNumber % base
        stack.push(rem)
        decNumber = decNumber // base

    result = ""

    while not stack.isEmpty():
        result = result + digits[(stack.pop())]

    return result


print(decToBin(54, 26))
print(decToBin(5478655656, 8))
