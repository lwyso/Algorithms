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

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print('You were born on {day}'.format(day=days[X]))

