"""
A sort-of cipher made by Darren Yap, 2021.
This cipher takes the ASCII printable characters (excluding whitespace), and reverses the string.
For instance, 'a' becomes '@'.
"""
import string as s

# constants
NORMAL = s.printable[:len(s.printable) - 6]
REV = NORMAL[::-1]

# swapping function
while True:
	string = input("enter a string: ")
	new_string = ''''''

	for i in string:
		if i != ' ':
			new_string += REV[NORMAL.index(i)]
		else:
			new_string += i
	print(new_string)