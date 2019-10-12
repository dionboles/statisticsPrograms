#
#
#num = 1/2 
#for i in range(4):
#	num = num * 1/2
#	print(num)
#
#
#print(round(num,6))

#num = 1/2 
#for i in range(9):
#	num = num * 1/2
	#	print(num)
#
#
#print(round(num,5))

#print(0.00098 * 10000)

#num = 99.4 /100 
#for i in range(5):
#	num = num * 99.4 /100 
#	print(num)
#	
#	
#answer = round(num,4) 
#print("answer {}".format(answer))
#
#complemnet = 1 - answer
#
#print(round(complemnet,4))
#		
		
#print(round(0.950703002,5))
#num =  0.97504
#for i in range(4):
#	num =  num * 0.97504
#	print(round(num,5))
#
#answer = round(num,5)
#complemnet = 1 - answer
#print(round(complemnet,5))

def clac (num,count,roundTO):
	tmp = num 
	count = count -1
	for i in range(count):
		num = num * tmp
		print(round(num,roundTO))
	answer = round(num,roundTO)
	print("answer {}".format(answer))
	complemnet = 1 - answer
	print("complemnet {}".format(round(complemnet,5)))
	



#
#clac(0.06, 6, 4)

import math


print(round(1-0.44**4,4))


print(0.1674
	+ 0.3356
	+ 0.2861
	+0.1479
	+0.0376
	+0.0254)
	
num = [0.1674,0.3356,0.2861,0.1479,0.0376,0.0254]

for i in range(5):
	print((i**2 * num[i]))
	
print(math.sqrt(15.700613760000001))



print(round(0.076923077,3))

