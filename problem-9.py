def generate_pythagorean_triplets(limit):
    triplets = []
    for m in range(2, int(limit**0.5) + 1):
        for n in range(1, m):
            if (m - n) % 2 == 1 and gcd(m, n) == 1:  # ensures primitive triplets
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                if c > limit:
                    break
                triplets.append((a, b, c))
    return triplets

def find_pythagorean_triplet_with_sum(total):
    for a in range(1, total):
        for b in range(a + 1, total - a):
            c = total - a - b
            if a * a + b * b == c * c:
                return (a, b, c)
    return None
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


triplets = find_pythagorean_triplet_with_sum(1000)

length = len(triplets)
for i in range(0, length):
  (a, b, c) = triplets[i]
  print(a, b, c)
  print("a + b + c:", a + b + c)
  if(a ** 2 + b ** 2 == c ** 2):
    if(a + b + c == 1000):
      print("a * b * c:", a * b * c)