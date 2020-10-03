class Square():
    def __init__(self,side = 1):
        self.side = side

    def area(self):
        print("Side length is "+ str(self.side))
        print("Area of square is:")
        return self.side**2

my_square = Square()           #### PUT VALUES OF LENGTH AND BREADTH HERE####
print(my_square.area())
