import pprint
bob2 = {'name': {'first': 'Bob', 'last': 'Smith'}, 'age': 42,
        'job': ['software', 'writing'], 'pay': (40000, 50000)}

print(bob2['name'])
# print the value to 'name' {'first'}: 'Bob', 'last' : 'Smith'}

print(bob2['name']['last'])  # grab bob's last name

print(bob2['name']['first'], bob2['name']['last'])
# grab both parts of Bob's name from nested object

print(bob2['pay'][1])  # bob's upper pay

for job in bob2['job']:
    print(job)

# print(bob2['job'][-1]) prints bob's last job which is 'writing'
bob2['job'].append('janitor')
print(bob2['job'])


# Dictionaries of dictionaries

bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')

db = {}

db['bob'] = bob
db['sue'] = sue

print(db['bob']['name'])
db['sue']['pay'] = 50000
print(db['sue']['pay'])  # prints sue's new pay of 50000

print(db)
pprint.pprint(db)

for key in db:
    print(key, '=>', db[key]['name'], ', ', db[key]['age'])

for key in db:
    print(key, '=>', db[key]['pay'])

for key in db:
    print(db[key]['name'].split()[-1])  # grabs last names
    db[key]['pay'] *= 1.10  # gives 10% raise
    print(db[key]['pay'])

for record in db.values():
    print(record['pay'])


x = [db[key]['name'] for key in db]
print(x)

x = [rec['name'] for rec in db.values()]
print(x)

# Assign a new record

db['tom'] = dict(name='Tom', age=50, job=None, pay=0)
print(db['tom'])
print(db['tom']['name'])
print(list(db.keys()))
print(len(db))
print([rec['age'] for rec in db.values()])
print([rec['name'] for rec in db.values() if rec['age'] >= 45])
