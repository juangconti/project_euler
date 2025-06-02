number = 1



def is_divisible_by_all(number, divisors):
    for divisor in divisors:
        remainder = number % divisor
        if number % divisor != 0:
            return False
    return True

while True:
    if is_divisible_by_all(number, range(11, 21)):
        print(f"The smallest number divisible by all numbers from 1 to 20 is: {number}")
        break
    else:
      number += 1111

print(number)
        
