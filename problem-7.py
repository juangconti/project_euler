prime = 0
primeCounter = 0
 
def isprime(n):
  if n < 2:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True


while primeCounter < 10002:
  prime += 1
  if(isprime(prime)):
    primeCounter += 1

print(f"The 10001st prime number is {prime}")

