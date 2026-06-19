def ifTriangle(sides):
    if (sides[0] * sides[1] * sides[2] != 0) * (sides[0] + sides[1] >= sides[2]) * (sides[1] + sides[2] >= sides[0]) * (sides[2] + sides[0] >= sides[1]):
        return True
    return False

def equilateral(sides):
    if ifTriangle(sides) * (sides[0] == sides[1]) * (sides[0] == sides[2]):
        return True
    return False

def isosceles(sides):
    if ifTriangle(sides) * ((sides[0] == sides[1]) + (sides[1] == sides[2]) + (sides[2] == sides[0])):
            return True
    return False

def scalene(sides):
    if equilateral(sides) + isosceles(sides) + (not ifTriangle(sides)):
        return False
    return True
    
