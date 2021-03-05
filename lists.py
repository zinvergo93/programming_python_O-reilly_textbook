bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']
# [name(0), age(1), salary(2), study(3)]
print(bob)  # values of list given for 'bob'
print(bob[0], sue[2])  # list bob's name and sue's salary
print(bob[0].split()[-1])  # what's bob's last name?
print(sue)  # values of list given for 'sue'
sue[2] *= 1.25  # give sue a 25% raise
print(sue)  # updated value of list for 'sue', with 'salary' now 50000.0 from 25% raise
print("&&&&&&")
people = [bob, sue]
for person in people:  # for loop that reads the values of each iterable as a single item
    print(person)               # prints values of 'bob' and 'sue' as single item


print(people[1][0])  # prints 'Sue Jones'

for person in people:
    print(person[0].split()[-1])  # prints last names from both 'bob' and 'sue'
    person[2] *= 1.20  # give each a 20% raise

for person in people:
    print(person[2])  # check for new pay

pays = [person[2] for person in people]  # collect all pay
print(pays)


pays = map((lambda x: x[2]), people)  # map is a generator in 3
list(pays)

# generator expression, sum built-in
total = sum(person[2] for person in people)
print(total)


people.append(['Tom', 50, 0, None])
print(len(people))
print(people)
print(people[-1][0])
