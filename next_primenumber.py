def is_primenum(num):

	if num > 1:
		for i in range(2,num):
			if num%i == 0:
				return False
			
		return True

	return "Not valid number bro!"

def gen_prime():

	 yield 2
	 num = 3
	 while(True):
	 	if is_primenum(num):
	 		yield num
	 	num += 2

choice = input("Continue finding prime numbers (y/n)? ")
current = 1

while choice.lower().startswith('y'):
	current += 1

	while is_primenum(current) == False:
		current += 1

	print("next prime number is "+str(current))
	choice = input("Continue finding prime numbers (y/n)? ")
