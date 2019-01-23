from pythonds.basic.queue import Queue

def hotPotato(names, num):

    queue = Queue()

    for name in names:
        queue.enqueue(name)
    
    # return queue.size()
    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
        
        print(queue.dequeue())
    return queue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
