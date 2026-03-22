list =[]
for i in range(0,10):
    entry = int(input("Give ten integer numbers from 10 to 20: "))
    while entry < 10 or entry > 20:
        entry = int(input("Wrong number! Give ten integer numbers from 10 to 20: "))
    list.append(entry)
print(list)

my_tuple = tuple(list)
print(my_tuple)

new_list = []
for i in range(0,10):
    new_list.append(list[i]**2)

new_list.sort()
print(new_list)

my_tuple2 = tuple(new_list)
print(my_tuple2)
