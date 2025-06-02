sumOfSquares = 0
squareOfSum = 0

for i in range (1, 101):
    sumOfSquares += i ** 2
    squareOfSum += i

print('Sum of squares:', sumOfSquares)
print('Square of sum:', squareOfSum ** 2)

print('Difference:', squareOfSum ** 2 - sumOfSquares)