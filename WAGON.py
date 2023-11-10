class Wagon:
    def __init__(self,GetOwnerName,GetWeight,GetNumberOfWheels):
        self.GetOwnerName = GetOwnerName
        self.GetWeight = GetWeight
        self.GetNumberOfWheels=GetNumberOfWheels
    
class ClosedWagon(Wagon):
    def __init__(self, height,NumberOfDoors,SuitableForFoodStuffs):
        self.Height = height
        self.NumberOfDoors = NumberOfDoors
        self.SuitableForFoodStuffs = SuitableForFoodStuffs

class OpenWagon(Wagon):
    pass


class Siding:
    def __init__(self):
        self.wagons = [None] * 30
        self.s=0

    def push(self, wagon):
        if self.wagons[self.s] is None:
            self.wagons[self.s] = wagon
            self.s=self.s+1
            return
        print("Siding is full")

    def pop(self):
        if self.wagons[self.s] != 0:
            wagon = self.wagons[self.s]
            self.wagons[self.s] = None
            self.s= self.s-1
            return wagon
        print("Sindings are empty")

class Yard:
    def __init__(self):
        self.sidings = []

    def add_siding(self, siding):
        self.sidings.append(siding)

    def remove_siding(self, siding):
        self.sidings.remove(siding)

yard1= Yard()
siding= Siding()
wagon1 = Wagon("ABC", "1000", "50")


siding.push(wagon1)
siding.push(wagon1)
