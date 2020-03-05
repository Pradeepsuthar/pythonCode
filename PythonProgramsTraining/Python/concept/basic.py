'to define some functions and variables'
MAX = 3000
print("Hello guys, you are using basic module")
if __name__=='__main__':
    print("I know that you are executing basic module directly")

def get_maintainance(size):
    'to calc monthly charge'
    if size >= 1000 and size <= 3000:
        rate = 0.9
    elif size<1000 and size>=0:
        rate = 1.1
    else:
        print("Invalid size, try again")
        return 0
    charge = size*rate*1.1
    return charge

def get_sum_digits(str):
    'to sum up all digits into str'
    sum = 0
    for ch in str:
        if ch.isdigit():
            sum += int(ch)
    else:
        print("sum is : %d" %sum)
