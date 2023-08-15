n = int(input())
unique_chemical = set()
for _ in range(n):
    compounds = input().split()
    for el in compounds:
        unique_chemical.add(el)

print(*unique_chemical, sep='\n')

