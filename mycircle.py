#alicia leslie
#5-9
#private class

import math

class circle:
    def __init__(self,radius=1):
        self.__radius=radius
        
    def getRadius(self):
        return self.__radius

    def getPerimeter(self):
        return 2*self.__radius*math.pi
    
    def getArea(self):
        return self.__radius*self.__radius*math.pi
    
    def setRadius(self,radius):
        self.__radius=radius
def main():
    circle1=circle(1)
    print("The area of the circle of radius",circle1.radius,"is", circle1.getArea())
    
    circle2=circle(25)
    print("The area of the circle of radius",circle2.radius,"is", circle2.getArea())
    
    circle3=circle(125)
    print("The area of the circle of radius",circle3.radius,"is", circle3.getArea())

    circle2.setRadius(100)
    print("The area of the circle of radius",circle2.setRadius,"is", circle2.getArea())
main()
