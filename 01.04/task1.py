import heapq

numbers = []
for i in range(int(input())):
    numbers.append(int(input()))

heapq.heapify(numbers)
time = 0

while len(numbers) > 1:
    a = heapq.heappop(numbers)
    b = heapq.heappop(numbers)
    s = a + b
    time += s
    heapq.heappush(numbers, s)

print(time)