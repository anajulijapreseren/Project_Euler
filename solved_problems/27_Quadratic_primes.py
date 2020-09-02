#n**2 + an + b
#|a| < 1000, |b| <= 1000
#n = 0

#n = 0 must produce prime so that means that b is prime(and of course > 0)

#print(len(candidates_b))
#168 candidates

#if we take even number for a:
#n= odd:odd+even+odd = even
#n = even:even + even + odd = odd
#so we can only insert one number before we don't get prime

#a can't be even
#if we write some examples we see that when a isn't prime we don't go very far--> so we take a is prime
#a can also be -1 * prime



def erathostens_sieve(n):
	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False
	for i in range(2,int(n**0.5+1)):
		index = i*2
		while index < n:
			is_prime[index] = False
			index = index+i
	prime = []
	for i in range(n):
		if is_prime[i] == True:
			prime.append(i)
	return prime

def is_prime(n):
	for i in range(2,int(abs(n)**0.5)+1):
		if n%i == 0:
			return False
	return True

primes1000 = erathostens_sieve(1000)
#copy list
primes = primes1000[:]

maxvalue_n = 0

for b in primes1000:
	for a in primes1000:
		n = 0
		while True:
			number = n**2 + a  *n + b
			if number not in primes:
				if is_prime(number):
					primes.append(number)
				else:
					if n-1 > maxvalue_n:
						maxvalue_n = n-1
						axb = a*b
					break
			n += 1
		n = 0
		#negative a and positive b
		while True:
			number = n**2-a*n + b
			if number not in primes:
				if is_prime(number) and number>0:
					primes.append(number)
				else:
					if n-1 > maxvalue_n:
						largest = n-1
						axb = -1*a*b
					break
			n += 1
print(axb)