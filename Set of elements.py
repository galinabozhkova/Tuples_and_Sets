n,m = input().split()
n = int(n)
m = int(m)

first_set = set()
second_set = set()

for i in range (0, n+m):
    if i <n:
        first_set.add(input())
    elif n<=i< n+m:
        second_set.add(input())

print(*(first_set&second_set), sep='\n')