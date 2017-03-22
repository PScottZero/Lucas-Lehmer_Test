from math import log
from time import time
from random import randint

def getLucas(index, modulo):
	prev = 4
	for x in range(1,index):
		prev = ( prev ** 2 - 2 ) % modulo
	return prev
	
def fermat(p):
	testPass = 0
	for a in range (2,7):
		if (a ** (p - 1)) % p == 1:
			testPass += 1
	if testPass == 5:
		return True
	else:
		return False
	
def getTime(start):
	total = time() - start
	hours = int(total / 3600)
	total = total % 3600
	minutes = int(total / 60)
	seconds = int(total % 60)
	print(str(hours) + "h " + str(minutes) + "m " + str(seconds) + "s elapsed since last Mersenne Prime found\n")
	return time()
		
try:
	power = 3
	print("M(2)\n3\n")
	start = time()
	start = getTime(start)
	while True:
		if fermat(power) == True or power == 3 or power == 5:
			value = 2 ** power - 1
			if getLucas(power - 1, value) == 0:
				print("M(" + str(power) + ")\n" + str(value) + "\n")
				start = getTime(start)
		power += 2
except KeyboardInterrupt:
	pass