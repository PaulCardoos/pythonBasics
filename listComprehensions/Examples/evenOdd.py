#print all even numbers without list comprehension from 1-100
even = []
for i in range(0, 101):
    if(i % 2 == 0):
        even.append(i)
print(even)

#same problem with list comprehension
even = [i for i in range(0,101) if i % 2 == 0]
print(even)

#print all odd numbers without list comprehension from 1-100
odd = []
for i in range(0, 101):
    if(i % 2 == 1):
        odd.append(i)
print(odd)

#same problem with list comprehension
even = [i for i in range(0,101) if i % 2 == 1]
print(odd)