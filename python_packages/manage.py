from myPackages import personalData as mypk
from myPackages.tree import serializer

clf = serializer.DecisionTree()

my_obj = mypk.MyPersonalInfoClass()

my_obj.myPersonalInfo()
my_obj.KinalPersonalInfo()

my_obj.speed('Swift Dizier')


area = clf.fit(8,2)

print("Area is",area)
