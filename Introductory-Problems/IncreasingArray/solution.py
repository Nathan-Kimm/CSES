size = input()
list = list(map(int, input().split()))
count = 0

for i in range(len(list)-1):
    if list[i] > list[i+1]:
         count += list[i] - list[i+1] 
         list[i+1] = list[i]
print(count)    