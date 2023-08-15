n = int(input())
first_set = set()
second_set = set()
lenght = 0
max_intersection = set()
for _ in range(n):
    first_interval, second_interval = input().split('-')
    first_interval = first_interval.split(',')
    second_interval = second_interval.split(',')
    for el in range (int(first_interval[0]), int(first_interval[1])+1):
        first_set.add(el)
    for el in range (int(second_interval[0]), int(second_interval[1])+1):
        second_set.add(el)
    intersection_set = first_set&second_set
    if len(intersection_set)> lenght:
        lenght = len(intersection_set)
        max_intersection = intersection_set
    first_set = set()
    second_set = set()

print(f'Longest intersection is {list(max_intersection)} with length {lenght}')


