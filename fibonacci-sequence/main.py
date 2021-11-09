sequence = []
x = 0 #the first term in the sequence
y = 1 #the second term in the sequence

print(x)
print(y)

while len(sequence) <= 1000000:
  sequence.append(x)
  sequence.append(y)
  z = x + y
  x = y
  y = z
  print(str(x) + "\n")
  print(str(y) + "\n")
  
