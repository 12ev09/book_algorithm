"""
n個の整数をいくつか足し合わせて、和が1以上W以下の整数となる整数は何通りか

→ dp[N][j] が Trueであるものが何個あるか
"""

N, W = map(int, input().split())
A = list(map(int, input().split()))

"""
dp[i][j] i番目まででいくつか選んだ総和がWに一致するかどうか
"""
dp = [[False for _ in range(W+1)] for _ in range(N+1)]

dp[0][0] = True

for i in range(N):
    for j in range(W+1):
        # A[i] を選ぶ場合
        if j-A[i] >= 0 and dp[i][j-A[i]]:
            dp[i+1][j] = True

        # A[i] を選ばない場合
        if dp[i][j]:
            dp[i+1][j] = True

ans = 0
for i in range(1, W+1):
    if dp[N][i]:
        ans += 1

print(ans)
