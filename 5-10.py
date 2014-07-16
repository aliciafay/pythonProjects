#alicia leslie
#5-10
#private class main

import mycircle

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
