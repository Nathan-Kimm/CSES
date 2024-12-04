#Very rough solution but it works
number = input()
list = list(map(int, input().split()))
list.sort()
if len(list) == 1:
    if list[0] == 1:  
        print(2)
        exit()
    else:
        print(1)
        exit()
for i in range(len(list)-1):
    if not (list[i+1]-list[i] == 1):
        print(list[i]+1)
        exit()
print(number)
