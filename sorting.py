import random

LENGTH = 20
LIMIT = 500


def sort_by_value(numbers):
    return sorted(numbers)


num_list = []
for i in range(LENGTH):
    num_list.append(random.randint(-LIMIT, LIMIT))

print(num_list)
print(sort_by_value(num_list))