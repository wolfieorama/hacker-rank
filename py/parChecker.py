from pythonds.basic.stack import Stack

def parChecker(symStr):
    index = 0
    balanced = True
    s = Stack()

    while index < len(symStr) and balanced:
        curr_sym = symStr[index]

        if curr_sym == "(":
            s.push(curr_sym)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        
        index += 1
    
    if s.isEmpty() and balanced:
        return True
    else:
        return False


print(parChecker("((()))"))
print(parChecker("())"))




