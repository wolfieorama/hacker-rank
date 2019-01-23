from pythonds.basic.deque import Deque
def palindrome(str):
    dq = Deque()
    ispalindrome = True
    for char in str:
        dq.addFront(char)
    while dq.size() > 1:
        if dq.removeFront() != dq.removeRear():
            ispalindrome = False
    return ispalindrome

print(palindrome("radar"))
print(palindrome("Banana"))


