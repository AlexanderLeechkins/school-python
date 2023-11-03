class stock_items:
    def __init__(self,)



class Book:
    def __init__(self,title,author,ISBN,OnLoan,DateAcquired):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.OnLoan = OnLoan
        self.DateAcquired = DateAcquired

    def display(self):
        print(f"the books name is {self.title}\n the author's name is {self.author}\n the ISBN number is {self.ISBN}\n and the date is {self.DateAcquired}\n")

    def setLoan(self):
        self.OnLoan = True
    
    def returnLoan(self):
        self.OnLoan = False

    
Harry_potter = Book("philosophers stone", "J.K Rowling", 311006, True,"23/09/2023")
Harry_potter.display()

class CD:
    def __init__(self,title,Artist,PlayingTime,OnLoan,DateAcquired):
        self.title = title
        self.Artist = Artist
        self.PlayingTime = PlayingTime
        self.OnLoan = OnLoan
        self.DateAcquired = DateAcquired

    def display(self):
        print(f"the CD's name is {self.title}\n the CD playtime is {self.PlayingTime}\n the Artists name is {self.Artist}\n the date of loan is {self.DateAcquired}\n")

    def setLoan(self):
        self.OnLoan = True
    
    def returnLoan(self):
        self.OnLoan = False

beatles= CD ("let it be", "Beatles", "3 min 50 sec",True,"23/09/2023")
beatles.display()







    

        
