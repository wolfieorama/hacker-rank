from pythonds.basic.stack import Stack

def decToBin(decNumber):

    stack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        stack.push(rem)
        decNumber = decNumber // 2

    result = ""

    while not stack.isEmpty():
        result = result + str(stack.pop())

    return result


print(decToBin(54))
print(decToBin(5478655656))
