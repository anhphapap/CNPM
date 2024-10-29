n=int(input())

# print((n*'*'+'\n')*n)

# for i in range(1, n+1):
#     print(i*'*')

# for i in range(1, n+1):
#     print((n-i)*' '+i*'*')

for i in range(1, n+1, 2):
    print((n-i)//2*' '+i*'*')

