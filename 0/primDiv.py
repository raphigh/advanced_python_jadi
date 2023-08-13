#import libraries 

import math


 
#define isprime function

def isPrime(num):
	if num < 2 :
		return False
	elif num == 2 or num  == 3:
		return True
	else:
		if num % 2 == 0 :
			return False
		for i in range(3,int(math.sqrt(num))+1,2):
			if num % i == 0 :
				return False

		return True


def cntPrimeDiv(num):
	cnt = 0
	for i in range(1,num+1):
		if num % i == 0 and isPrime(i):
			cnt += 1
	return cnt

	
#input unit
lst = []
for i in range(10):
	n = int(input())
	lst.append(n)


#process
max_num = lst[0]
max_div = cntPrimeDiv(lst[0])

for i in lst[1:]:
	if cntPrimeDiv(i) >= max_div:
		max_num = max(i,max_num)
		max_div = cntPrimeDiv(i)

print(max_num,max_div)
	
