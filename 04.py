#program to sum of n digit
def getsum(n) :
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

n =199999
print(getsum(n))