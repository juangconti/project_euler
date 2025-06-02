limit = 2000000
sumOfPrimes = 0

def isprime(n):
  if n < 2:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

for i in range(2, limit):
  if(isprime(i)):
    sumOfPrimes += i

print(sumOfPrimes)