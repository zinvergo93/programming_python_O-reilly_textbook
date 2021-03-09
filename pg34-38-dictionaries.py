# sue = {}
# sue['name'] = 'Sue Jones'
# sue['age'] = 45
# sue['pay'] = 40000
# sue['job'] = 'hdw'

# print(sue)

# names = ['name', 'age', 'pay', 'job']
# values = ['Sue Jones', 45, 40000, 'hdw']
# list(zip(names, values))
# sue2 = dict(zip(names, values))
# print(sue2)


# fields = ('name', 'age', 'job', 'pay')
# record = dict.fromkeys(fields, '?')
# print(record)


bob = {'pay': 30000, 'job': 'dev', 'age': 42, 'name': 'Bob Smith'}
sue = {'pay': 40000, 'job': 'hdw', 'age': 45, 'name': 'Sue Jones'}

people = [bob, sue]

for person in people:
    print(person['name'], person['pay'], sep=', ')

names = [person['name'] for person in people]
print(names)

all_pay = sum(person['pay'] for person in people)
print(all_pay)  # prints 70000 (sum of 30000 and 40000)

# SQL-like query, will print ['Sue Jones']
sql_sue = [rec['name'] for rec in people if rec['age'] >= 45]
print(sql_sue)


a = [(rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people]
# prints [42, 2025], 2025 being 45**2, while 42 doesn't meet conditional requirements of >=45
print(a)

G = (rec['name'] for rec in people if rec['age'] >= 45)
print(next(G))

G_two = ((rec['age']**2 if rec['age'] >= 45 else rec['age']) for rec in people)
print(G_two.__next__())  # ????? prints 42, research __next__

for person in people:
    print(person['name'].split()[-1])  # grabs both last names
    person['pay'] *= 1.10  # gives both people a 10% raise to their pay

for person in people:
    print(person['pay'])  # prints new pay
