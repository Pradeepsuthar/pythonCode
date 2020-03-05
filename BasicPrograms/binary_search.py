# Binary Search
a = [1,5,7,8,11,13,16]

def binary_search(a, key, start, end):
    if start <= end:
        mid = int((start+end)/2)
        if a[mid] > key:
            return binary_search(a, key, start, mid-1)
        elif a[mid] < key:
            return binary_search(a, key, mid+1,end)
        else:
            print(key,"is found")
    else:
        print(key,"not found")


print(binary_search(a, 19,0, len(a)-1))
