# NAME, AGE, PAY = range(3)  # assigns variable to each index in the range of 3
# bob = ['Bob Smith', 42, 10000]
# mary = ['Mary Rogers', 38, 30000, 'development']
# print(bob[NAME])
# print(bob[AGE])
# print(bob[PAY])
# print(mary[NAME])
# print(mary[AGE])
# print(mary[PAY])
# # prints 'development' as it's value is index of 3, even though it is in a range of 4
# print(mary[3])
# # prints index value of PAY and then it's value as it's called
# print(PAY, ",", bob[PAY])

# bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
# sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
# people = [bob, sue]

# print(bob)
# print(sue)

# for person in people:
#     print(person[0][1], person[2][1])  # name, pay

# print([person[0][1] for person in people])  # collect names

# for person in people:
#     print(person[0][1].split()[-1])  # get last names
#     person[2][1] *= 1.10  # give each 10% raise

# for person in people:
#     print(person[2])

# for person in people:
#     for (name, value) in person:
#         if name == 'name':
#             print(value)  # find specific field


# def field(record, label):
#     for (fname, fvalue) in record:
#         if fname == label:  # find any field by name
#             return fvalue


# print(field(bob, 'name'))
# print(field(sue, 'pay'))

# for rec in people:
#     print(field(rec, 'age'))  # print all ages
