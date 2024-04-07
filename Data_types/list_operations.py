l1=[10,20,30,40]
del l1[0:3]
print(l1)


# Copy function example
# shallow copy
print("-"*25,"shallow copy example","-"*25)
l1=[10,20,30,40]
l2=l1.copy()
print(l1,id(l1))
print(l2,id(l2))

# Deep copy
print("-"*25,"Deep copy example","-"*25)
l1=[True,1,5,4.3]
l2=l1
print(l1,id(l1))
print(l2,id(l2))

# slice based copy  
l1 = [1,44,92,9.33,'hello']
l2 = l1[0:3]
print(l1)
print(l2)

l1=[10,20,30,40,10,28,10]
ba = bytearray(l1)

print(ba)

ba[4] = 55

print(ba)
