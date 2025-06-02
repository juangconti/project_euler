import textwrap

powerDigitSum = 2 ** 1000

stringOfNumber = str(powerDigitSum)

def sum_of_digits(number):
  digits = textwrap.wrap(number, 1)
  length = len(digits)
  sum = 0
  for i in range(0,length):
    sum += int(digits[i])

  return sum

print(sum_of_digits(stringOfNumber))