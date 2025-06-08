maxSequence = 0
number = 15
buffer = 0
sequenceCount = 0


def get_collatz_sequence_terms(number):
  sequenceCount = 1
  while(int(number) != 1):
    sequenceCount += 1
    if(number % 2 == 0):
      number = number / 2
    else:
      number = 3*number + 1 

  return sequenceCount


for i in range(999999, 1, -1):
  sequenceCount = get_collatz_sequence_terms(i)
  if(sequenceCount > maxSequence):
    maxSequence = sequenceCount
    buffer = i

print(maxSequence)
print(buffer)
