value = int(input())
result = str(value) + " "
while(value != 1):
    if value%2 == 0:
        #// does floor division so drops decimal
        value //= 2
        result += str(value) + " "
    else:
        value = value * 3 + 1
        result += str(value) + " "
print(result)