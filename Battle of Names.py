n = int(input())
odd_set = set()
even_set = set()

for i in range(1, n + 1):
    name = input()
    ascii_sum = 0

    for letter in name:
        ascii_sum += ord(letter)

    if int(ascii_sum / i) % 2 == 0:
        even_set.add(int(ascii_sum / i))
    else:
        odd_set.add(int(ascii_sum / i))

if sum(even_set) == sum(odd_set):
    print(*(odd_set | even_set), sep=', ')
elif sum(odd_set) > sum(even_set):
    print(*(odd_set - even_set), sep=', ')
elif sum(even_set) > sum(odd_set):
    print(*(odd_set ^ even_set), sep=', ')

