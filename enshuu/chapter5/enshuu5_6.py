"""
N個の整数を選んで総和をWに一致させることができるか(N個それぞれに対して使える個数が設定されている)
"""

INF  = 1<< 30
N,W  = map(int,input().split())
A = list(map(int,input().split()))
M = list(map(int,input().split()))

"""
dp[i][j]: i個目までで総和がjになる方法のうち、最後の整数を用いる回数の最小値
"""
dp = [[INF for _ in range(W+1)] for _ in range(N+1)]

dp[0][0] = 0

for i in range(N):
    for j in range(W+1):
            # dp[i+1][j-A[i]] < M[i] → さらに追加でA[i]を用いることができる
            if j - A[i] >= 0 and dp[i+1][j-A[i]] < M[i]:
                dp[i+1][j] = min(dp[i+1][j],dp[i][j-A[i]]+1)
            # A[i]を選ばない場合
            dp[i+1][j] = min(dp[i+1][j],0)

print("Yes") if dp[N][W] < INF else print("No")