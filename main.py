n = int(input())
data = input().split()
checked_numbers = [0]*n
print(0,1,2,3,4,5,6,7)
for number in data:
    if checked_numbers[int(number)]:
        print(number)
        break
    checked_numbers[int(number)] = 1