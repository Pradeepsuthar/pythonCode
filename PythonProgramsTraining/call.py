import math
duration = 120
rate = 1.5
min = math.ceil(duration/60)
cost = rate*min
print("Cost of call Rs.",cost,"per minute")