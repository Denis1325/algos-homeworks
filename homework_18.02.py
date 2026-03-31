n = int(input())
data = list(map(int, input().split()))

slow = n - 1 # число n-1 точно не в цикле (нет указателя на него)
fast = n - 1
while True:
    slow = data[slow]
    fast = data[data[fast]]
    if slow == fast:
        break

a = slow

b = n-1
while a != b:
    a = data[a]
    b = data[b]

print(a)
