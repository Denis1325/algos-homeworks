import heapq

numbers = []
n = int(input())
for i in range(n):
    numbers.append(int(input()))
k = int(input())

heap = []
result = []
for i in range(len(numbers)):
    value = numbers[i]
    heapq.heappush(heap, (-value, i))          # -value, т.к. heapq использует min-heap
    if i >= k - 1:
        while heap and heap[0][1] <= i - k:
            heapq.heappop(heap)
        result.append(str(-heap[0][0]))
print(' '.join(result))