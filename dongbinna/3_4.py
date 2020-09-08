N, K = map(int, input().split())

cnt = 0
while (N != 1):
    target_num = N // K
    cnt += N - (target_num * K)
    N = target_num * K

    if N < K:
        break

    cnt += 1
    N = N // K

cnt += N - 1
print(cnt)
