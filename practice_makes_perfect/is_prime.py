def is_prime(x):
	for n in range(2, x-1):
		print(n)
		if x % n == 0:
			print(False)
		else:
			print(True)

is_prime(0)