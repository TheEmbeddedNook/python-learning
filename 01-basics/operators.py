############################
##Airthmatic operators
############################
print("Airthmatic operators result")
a = 15
b = 4

print(f"a = {a}")
print(f"b = {b}")

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)


#############################
##Comparison operators
############################# 
print("comparison operators result") 
speed = 80
limit = 100

print(speed == limit)
print(speed != limit)
print(speed > limit)
print(speed < limit)
print(speed >= limit)
print(speed <= limit)

##############################
##Logical operators
##############################
print("logical operators result")
ignition = True
doors_closed = True

print(ignition and doors_closed)

print(ignition or False)

print(not ignition)

########################
##Assignment operators
########################
print("assignment operators result")
counter = 10

counter += 5
print(counter)

counter *= 2
print(counter)

counter -= 4
print(counter)

########################
##Membership operators
########################
print("membership operators result")
project = "Radar Gen"

print("Radar" in project)

print("Camera" in project)

#########################
##Identity operators
#########################
print("identity operators result")
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)

print(a is b)

print(a == c)

print(a is c)