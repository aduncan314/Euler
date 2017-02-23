#Library of prime number related functions
#by Andrew Duncan 2016

import math
from types import *

# Despite the confusing name, takes a number and tests to see if it is prime
def	prime_test(number):
	try:
		is_prime = True
		break_point = math.sqrt(number)
		i = 2
		while i <= break_point and is_prime:
			if number % i == 0:
				is_prime = False
			i += 1
	except ValueError:
		is_prime = False
	return	is_prime

# Takes a given number and finds the first prime that is strictly larger
# Does not work for number<2
def next_prime_up(number):
	
	number = int(number)
	assert number >= 0
	
	if not number%2:
		iter = number + 1
		if number == 0:
			iter = 2
	else:
		iter = number + 2
	while not prime_test(iter):
		iter += 2
	return iter



def next_prime_down(number):
	
	number = int(number) + 1
	
	if not number%2 and number != 2:
		iter = number - 1
	elif number > 3:
		iter = number - 2
	elif number == 3:
		iter = 2
	elif number == 2:
		iter = -1
		print "Empty set"
	while not prime_test(iter) and (iter > 2):
		iter -= 2
	return iter


#sieve instead
def nth_prime(prime_index):

	num = 2
	for t in range(prime_index-1):
		num = next_prime_up(num)

	return num




#return factors too
#
#def	prime_test(number, Factors):
#	
#	is_prime = True
#	break_point = math.sqrt(number)
#	i = 2
#	while i <= break_point and is_prime:
#		if number % i == 0:
#			is_prime = False
#		i += 1
#	return	is_prime