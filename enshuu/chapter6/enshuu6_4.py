INF = 1 << 20
N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

"""
最小値をK以上にできるか?
できない→ 最小値はKより小さい
"""
ok = 0
ng = INF

while ng - ok > 1:
    mid = (ng+ok)//2

    # 区間幅をmidにできた個数
    prev = 0
    # 初期状態
    cnt = 1
    for i in range(N):
        if A[i] > A[prev] >= mid:
            cnt += 1
            prev = i

    if cnt >= M:
        ok = mid
    else:
        ng = mid

print(ok)
