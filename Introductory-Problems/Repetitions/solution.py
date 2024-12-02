sequence = input()
list = list(sequence)
count = 1
greatestCount = 1
for i in range(len(list)-1):
    word = list[i]
    if list[i] == list[i+1]:
        count += 1
    else:
        count = 1
    greatestCount = max(greatestCount, count)
print(greatestCount)