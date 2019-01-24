class Deque:
    def __init__(self):
        self.items = []

    def addFront(self,item):
        return self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def palindrome(str):

    dq = Deque()
    ispali = True

    for char in str:
        dq.addFront(char)

    while dq.size() > 1:
        if dq.removeFront() != dq.removeRear():
            ispali = False

    return ispali

print(palindrome("radar"))
print (palindrome("banana"))