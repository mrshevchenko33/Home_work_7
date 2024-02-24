my_list = [1, 0, 13, 0, 0, 0, 5, 2, 3, 4]

element = 0

count_list = my_list.count(0)

for _ in range(count_list):
    my_list.remove(element)
    my_list.append(element)
print(my_list)