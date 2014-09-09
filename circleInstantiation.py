#alicia leslie
#circle instantiation

import circleprogram

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
