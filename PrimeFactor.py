#!/bin/python

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import math, sys
sys.path.insert(0, '/Users/aduncan/Documents/Code/libduncan')
import primestuff as PS

def largest_prime(num):
	divisor = 2
	while num > 1:
		if not num%divisor:
			num = num/divisor
			print divisor
		else:
			divisor = PS.next_prime_up(divisor)
	return divisor

#print LargestPrime(600851475143)
#print LargestPrime(1000935479483928)
print largest_prime(1337)