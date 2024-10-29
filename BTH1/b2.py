n = int(input())
a = [int(input(f"a[{i}] = ")) for i in range(n)]
print(max(a) if max(a) > 0 else '*')
print(min(a) if min(a) < 0 else '*')
for x in set(a):
    print(f"{x} xh {a.count(x)}")
k = int(input('k = '))
for x in set(a):
    print(x if a.count(x) == k else "")
print('sort:')
a.sort(reverse=True)
for i in a:
    print(i)

