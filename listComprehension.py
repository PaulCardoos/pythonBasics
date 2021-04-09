#lists in python do not need to be of the same type
random = [1,2, "a", 1.21, "Im Paul"]

print(random)
#[1, 2, 'a', 1.21, 'Im Paul']

#iterate through the list using list comprehensions

#general syntax for list comprehension 
#[expression for val in list]
x = [print(i) for i in random]

#we can add an if statement to a list comprehension
#now we will only print if type is a string
x = [print(i) for i in random if type(i) == type("string")]

#you can add more than one if statement
#it will only print if both are true
names = ["Tom", "Jim", "Alan", "Greg", "Steve", "Sean", "Sarah"]

#only print if length of i is greater than 3 and last letter is h
x = [print(i) for i in names if len(i) > 3 and i[-1] == "h"]
#the result is only Sarah

