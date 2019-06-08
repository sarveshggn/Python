class Rectangle():
    def __init__(self,length,breadth = 1):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Length is "+ str(self.length))
        print("Breadth is "+ str(self.breadth))
        print("Area of rectangle is:")
        return self.length*self.breadth

my_rectangle = Rectangle()           #### PUT VALUES OF LENGTH AND BREADTH HERE####
print(my_rectangle.area())
