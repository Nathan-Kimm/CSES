number = int(input())

if number == 2 or number == 3:
    print("NO SOLUTION")
else:
    #range(starting value, end point, increment amount)
    for i in range(2, number + 1, 2):
        print(i, end = " ")
    for i in range(1, number + 1, 2):
        print(i, end = " ")