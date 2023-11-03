class Stock_items:
    def __init__(self,title,Creator,DateAcquired):
        self.title = title
        self.Creator = Creator 
        self.DateAcquired = DateAcquired
        self._OnLoan= False
    
    def setLoan(self):
        self._OnLoan = True

    def ReturnLoan(self):
        self._OnLoan = False    

class Book(Stock_items):
    def __init__(self,title,Creator,ISBN,DateAcquired):
        super(). __init__ (title,Creator,DateAcquired)
        self.ISBN = ISBN
        
    def display(self):
        print(f"the books name is {self.title}\n the author's name is {self.Creator}\n the ISBN number is {self.ISBN}\n and the date is {self.DateAcquired}\n")

class CD(Stock_items):
    def __init__(self,title,Creator,PlayingTime,DateAcquired):
       super(). __init__(title,Creator,DateAcquired)
       self.PlayingTime = PlayingTime
    

    def display(self):
        print(f"the CD's name is {self.title}\n the CD playtime is {self.PlayingTime}\n the Artists name is {self.Creator}\n the date of loan is {self.DateAcquired}\n")

    

beatles= CD ("let it be", "Beatles", "3 min 50 sec","23/09/2023")
beatles.display()

Harry_potter = Book("philosophers stone", "J.K Rowling", 311006,"23/09/2023")
Harry_potter.display()







    

        
