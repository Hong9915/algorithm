class chess:
    def __init__(self):
        self.king = 1
        self.queen = 1
        self.look = 2
        self.bishop = 2
        self.knight = 2
        self.poon = 8
    def difference(self,king, queen, look, bishop, knight, poon):
        print(f"{self.king - king} {self.queen - queen} {self.look - look} {self.bishop - bishop} {self.knight - knight} {self.poon - poon}")

a=chess()
numbers = input()
number=numbers.split()
a.difference(int(number[0]),int(number[1]),int(number[2]),int(number[3]),int(number[4]),int(number[5]))

    