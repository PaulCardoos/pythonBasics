#get all squares from 1-100 without list comprehensions
squares = []
for i in range(1,101):
    squares.append(i**2)
print(squares)

#same problem as above using list comprehension
squares = [i**2 for i in range(0, 101)]
print(squares)



