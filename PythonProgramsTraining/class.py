class Point:
    'to decribe/represent co-ordinate point by x,y,z'
    def __init__(self,x,y,z):
        'to describe a point'
        self.X=x
        self.Y=y 
        self.Z=z 

    def __str__(self):
        str="X :%0.2f\tY :%0.2f\tZ :%0.2f"%(self.X,self.Y,self.Z)
        return str
    
    def __add__(self,other):
        if type(other) in [int,float]:
            x=self.X + other 
            y=self.Y + other 
            z=self.Z + other
            return Point(x,y,z) 
        else:
            x=self.X+other 
            y=self.Y+other 
            z=self.Z+other
            return Point(x,y,z) 

     def __sub__(self,other):
        if type(other) in [int,float]:
            x=self.X - other 
            y=self.Y - other 
            z=self.Z - other
            return Point(x,y,z) 
        else:
            x=self.X-other 
            y=self.Y-other 
            z=self.Z-other
            return Point(x,y,z) 
pt1=Point(1,2,3)
pt2=Point(4,5,6)
pt3=pt1+pt2
print(pt3)
pt4=pt1+10
print(pt4)
print("Distance between two points:-",pt2-pt1)
print("Distance between first point and (10,10,10):"pt1-10)

