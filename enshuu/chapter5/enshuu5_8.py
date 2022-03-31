"""
N個の整数をM個の区間に分けたときの各区間の平均値の総和の最大値
"""

INF = 100000000000000000
N, M = map(int, input().split())
A = list(map(int, input().split()))

#  区間[j,i)の平均値を求める
f = [[0.0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(0, i):
        sum = 0.0
        for k in range(j, i):
            sum += A[k]
        f[j][i] = sum/(i-j)

"""
dp[i][k] 最初のi個について、k個の区間に分けたとき、最適な分割をしたときのスコア
"""

dp = [[-INF for _ in range(M+1)] for _ in range(N+1)]
dp[0][0] = 0

for i in range(0, N+1):
    for j in range(0, i):
        for k in range(1, M+1):
            dp[i][k] = max(dp[i][k], dp[j][k-1] + f[j][i])

ans = -INF
for i in range(0, M+1):
    ans = max(ans, dp[N][i])

print(ans)
