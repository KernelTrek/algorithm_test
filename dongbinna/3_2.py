import sys

N, M, K = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().rstrip().split()))

nums.sort()
m1 = nums[-1]
m2 = nums[-2]

result = ((m1 * K) + m2 ) * (M // (K + 1)) + m1 * (M % (K + 1))
print(result)
