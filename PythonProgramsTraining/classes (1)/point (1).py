class Point:
    'to represent a point by x,y and z'

    def __init__(self,x,y,z):
        'to initialize a point by x,y and z'
        self.X = x
        self.Y = y
        self.Z = z

    def __str__(self):
        'to display an object details'
        str = "X : %0.2f\tY : %0.2f\tZ : %0.2f"%(self.X,self.Y,self.Z)
        return str

    def __add__(self,other):
        'to add 2 obj of point'
        if type(other) in [int, float]:
            x = self.X+other
            y = self.Y+other
            z = self.Z+other
            return Point(x,y,z)
        else:
            x = self.X+other.X
            y = self.Y+other.Y
            z = self.Z+other.Z
            return Point(x,y,z)

p1 = Point(10,20,30)
p2 = Point(40,50,60)

print(p1)
print(p2)

p3 = p1+p2
print(p3)

p4 = p1+5
print(p4)

# built in attributes
print(Point.__dict__)
print(Point.__doc__)
print(Point.__name__)
print(Point.__module__)
print(Point.__bases__)