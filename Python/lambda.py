#dictionary is inside of list E.g.nested data structure list inside dictionary
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco" , "house" : "Slytherin"}
]
def f(person):
    return person["house"]

people.sort(key=f)
    
print(people)


#same as defining function f below one in lambda expression
people.sort(key=lambda person: person["name"])