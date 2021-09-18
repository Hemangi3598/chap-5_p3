# wapp to read a string and count the number of 
# lowercase and uppercase letters

s1 = input(" enter a string ")
lc, uc = 0, 0

for s in s1:
	if s.islower():
		lc = lc + 1
	elif s.isupper():
		uc = uc + 1
print(lc, uc)