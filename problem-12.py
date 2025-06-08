import math

numOfDivisors = 0

def isprime(n):
  if n < 2:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def get_quantity_of_divisors(number):
  quantity = 0
  for i in range(1, int(math.sqrt(number)+1)):
    if(number % i == 0):
      quantity +=1
  return quantity

def count_divisors_prime_factorization(n):
      count = 1
      i = n
      while i * i <= n:
          power = 0
          while n % i == 0:
              power += 1
              n //= i
          if power > 0:
              count *= (power + 1)
          i += 1
      if n > 1:
          count *= 2
      return count

term = 1
triangleNumber = 1
listOfTriangleNumbers = []
while(numOfDivisors < 500):
  triangleNumber = int((term * (term + 1))/2)
  numOfDivisors = count_divisors_prime_factorization(triangleNumber)
  term +=1
  if(numOfDivisors == 500):
    print(triangleNumber)
    break

print(triangleNumber)
print(numOfDivisors)