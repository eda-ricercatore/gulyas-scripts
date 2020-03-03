#!/usr/local/bin/python3

print("======================================")
print("=	Start Here	=")
for i in range(10):
	print("The index is:",i,"=")

print("======================================")
for i in [8,16,32,64,128,256,512,1024]:
	print("Current power of 2 is:",i,"=")


print("======================================")

powers_of_two = [ 2**power for power in range(3,10+1)]

for i in powers_of_two:
	print("Currently enumerated power of 2 is:",i,"=")




print("======================================")
print("=	End Here	=")