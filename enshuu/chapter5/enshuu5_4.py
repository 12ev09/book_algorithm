"""
N個の整数をK個以下を満たす範囲で選んだとき、Wに一致させることができるか
"""

INF = 1 << 30

N, W = map(int, input().split())
A = list(map(int, input().split()))
k = int(input())

"""
dp[i][j]: i個目までで総和がjになるように選んだ個数の最小値
"""
dp = [[INF for _ in range(W+1)] for _ in range(N+1)]

dp[0][0] = 0

for i in range(N):
    for j in range(W+1):
        # A[i]を選ぶ場合
        dp[i+1][j] = min(dp[i+1][j], dp[i][j-A[i]]+1)
        # A[i]を選ばない場合
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])

print("Yes") if dp[N][W] <= k else print("No")
