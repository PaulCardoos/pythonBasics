#the following is a list of tuples containing the model of cars and the year of the mdoel
cars = [
    ("Ford Escape", 2009), 
    ("Ford Fusion", 2010), 
    ("Mercedes Benz A-Class", 2021), 
    ("Jeep Wrangler", 2017), 
    ("BMW M5", 2019), 
    ("Mercedes Benz C-Class", 2016), 
    ("Toyota Tundra", 2018), 
    ("Buick Regal", 2005), 
    ("Buick Lacrosse", 2001), 
    ("Jeep Cheroke", 1999), 
    ("Honda Accord", 2013), 
    ("Ford Escape", 2012), 
    ("Hyundai Elantra", 2006), 
]

#we want all cars produced after 2015 with list comprehension
carsProducedAfter15 = []
for (car, model) in cars: 
    if model > 2015:
        carsProducedAfter15.append((car, model))
print(carsProducedAfter15)

#the same with a list comprehension
carsAfter15 = [(car, model) for (car, model) in cars if model > 2015]
print(carsAfter15)

#make a list comprehension do find all Ford
Fords = [(car, model) for (car, model) in cars if car[0] == "F"]
print(Fords)

#can you make a list comprehension for only print all cars made before 2010?