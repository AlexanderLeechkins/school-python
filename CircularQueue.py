queue= []
queuesize= 10
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
        if (R+1) % queuesize== f:
            print("the queue is full")
        else:
            R= R+1
            queue.insert(R, item)
def removeitem():
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
            f= (f+1) %queuesize
        
def queue_full():
    global f
    global R
    if (R+1) % queuesize == f:
        print("queue is full")   
    else:
        print("queue is not full")

def queue_empty():
    global f
    global R
    if f == -1 and R== -1:
        print("queue empty")
    else:
        print("queue is not empty")

input_of_user= 0
while input_of_user != 6:
    input_of_user= int(input("what would you like to do (add:1, remove:2, check full:3, check empty:4, print queue:5 or quit:6)"))
    if input_of_user == 1:
        addItem(input("what item would you like to add "))
    if input_of_user == 2:
        removeitem()
    if input_of_user == 3:
        queue_full()
    if input_of_user==4:
        queue_empty()
    if input_of_user== 5:
        print(queue)







