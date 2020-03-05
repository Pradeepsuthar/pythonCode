a = [51, 61, 1, 13, 71, 18, 19, 11, 21, 14]


for i in range(1,len(a)):
    key = a[i]
    j = i-1
    while j >= 0 and a[j] > key:
        a[j+1] = a[j]
        j-=1
    a[j+1] = key
print(a)