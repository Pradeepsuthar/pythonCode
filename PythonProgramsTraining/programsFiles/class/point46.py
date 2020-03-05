
class Point:
    'to describe/represent co-ordinate point by x, y, z'

    def __init__(self, x, y, z):
        'to initialize a point'
        self.X = x
        self.Y = y
        self.Z = z
    
    def __str__(self):
        'to display an object'
        str="X : %0.2f\tY : %0.2f\tZ : %0.2f" %(self.X,self.Y,self.Z)
        return str

    def __add__(self, other):
        'to add 2 instances of point'
        if type(other) in [int, float]:
            x = self.X+other
            y = self.Y+other
            z = self.Z+other
        else:
            x = self.X+other.X
            y = self.Y+other.Y
            z = self.Z+other.Z
        return Point(x, y, z)

# creating objects
pt1 = Point(5, 7, 9)
pt2 = Point(10, 15, 20)
pt3 = pt1+pt2
print( pt1 )
print( pt2 )
print( pt3 )
# moving an object
pt4 = pt1+10
print( pt4 )
# built-in attrbiutes
print( Point.__dict__ )
print( Point.__doc__)
print( Point.__name__)
print( Point.__module__)
print( Point.__bases__ )



