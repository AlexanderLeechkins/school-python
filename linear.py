queue= []
queuesize=0
f= -1
R=-1
def addItem(item):
    global f
    global R
    if f==-1 and R==-1:
        f=0
        R=0
        queue.insert(R, item)
    else:
        if (R+1)== queuesize:
            print("the queue is full")
        else:
            R= R+1
            queue.insert(R, item)
def removeitem(item2):
    global f
    global R
    if f==-1 and R==-1:
        print("queue empty")
    else: 
        item= queue.pop(f)
        if f ==R:
            f = -1
            R =-1 
        else:
            f=f+1
            
addItem(1)
print(queue)
addItem(2)
addItem(3)
addItem(4)
addItem(5)
addItem(6)
addItem(7)
addItem(8)
addItem(9)
print(queue)



