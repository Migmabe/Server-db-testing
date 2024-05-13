from string import ascii_letters, digits
import random
a = list(ascii_letters + digits)
random.shuffle(a)
dictionary = {}
k = 0
for _ in a:
	dictionary[k] = a[k]
	k += 1
dictionary[k] = " "
dictionary[k+1] = "."
print(dictionary)
