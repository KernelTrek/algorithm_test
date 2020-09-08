# 숫자 카드 게임 ( 로우별 최소 이면서, 행렬 상 최대 값 찾기 )
import sys

N, M, K = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().rstrip().split()))

nums.sort()
m1 = nums[-1]
m2 = nums[-2]

result = ((m1 * K) + m2 ) * (M // (K + 1)) + m1 * (M % (K + 1))
print(result)
