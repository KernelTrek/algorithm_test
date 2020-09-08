x, y = map(int, input().split())

l = list()
answer = 0
for _ in range(x):
    l.append(list(map(int, input().split())))

for nums in l:
    answer = max(answer, min(nums))

print(answer)

