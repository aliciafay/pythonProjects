#alicia leslie
#5-7
#class definition

import math

class circle:
    def __init__(self,radius=1):
        self.radius=radius
    #methods
    def getPerimeter(self):
        return 2*self.radius*math.pi
    def getArea(self):
        return self.radius*self.radius*math.pi
    def setRadius(self,radius):
        self.radius=radius
def main():
    circle1=circle()
    print("The area of the circle of radius",circle1.radius,"is", circle1.getArea())
    
    circle2=circle(25)
    print("The area of the circle of radius",circle2.radius,"is", circle2.getArea())
    
    circle3=circle(125)
    print("The area of the circle of radius",circle3.radius,"is", circle3.getArea())

    circle2.radius=100
    print("The area of the circle of radius",circle2.radius,"is", circle2.getArea())
main()
