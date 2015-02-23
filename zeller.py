#Zeller's algorithm to check which day of the week you were born

D = int(input("Date(DD):"))
M = int(input("Month(MM):"))
Y = int(input("Year(YYYY):"))

if M < 3:
	M = M + 12
	Y = Y - 1

F = int(Y/100)
L = Y - (100*F)

S = int(2.6*M-5.39) + int(L/4) + int(F/4) + D + L - 2*F

X = S - (7*int(S/7))

if X == 1:
	print('You were born on Monday')
elif X == 2:
	print('You were born on Tuesday')
elif X == 3:
	print('You were born on Wednesday')
elif X == 4:
	print('You were born on Thursday')
elif X == 5:
	print('You were born on Friday')
elif X == 6:
	print('You were born on Saturday')
elif X == 0:
	print('You were born on Sunday')
