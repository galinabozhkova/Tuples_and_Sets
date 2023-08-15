n = int(input())
unique_users = set()
for _ in range (n):
    unique_users.add(input())

# print('\n'.join(unique_users))
print( *unique_users, sep = '\n')
