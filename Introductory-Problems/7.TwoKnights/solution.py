num = int(input())

def calculateSquares(n):
    totalSquares = (n**2 * (n**2-1))//2
    knightPositions = 4 * (n-1) * (n-2)
    print(totalSquares - knightPositions)

for i in range(1, num+1):
    calculateSquares(i)