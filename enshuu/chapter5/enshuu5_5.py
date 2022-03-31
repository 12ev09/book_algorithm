"""
    いくつか足し合わせてWに一致させられるか(但し同じものを何個足しても良い)
"""

N, W = map(int, input().split())
A = list(map(int, input().split()))

"""
    dp[i][j] :i番目までみたときjに一致させられるか
    0 < j <= W 
"""

dp = [[False for _ in range(W+1)] for _ in range(N+1)]

dp[0][0] = True

for i in range(N):
    for j in range(W+1):
        # A[i] を選ぶ場合
        if j-A[i] >= 0 and dp[i+1][j-A[i]]:
            dp[i+1][j] = True

        # A[i] を選ばない場合
        if dp[i][j]:
            dp[i+1][j] = True

print(dp)
print("Yes") if dp[N][W] else print("No")
