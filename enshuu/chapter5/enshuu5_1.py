"""
input 
5
1 2 3
2 4 5
2 4 4
2 4 4
5 2 2

output
20
"""

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
# A = [[0,0,0]]+[list(map(int,input().split())) for _ in range(N)] 0indexが嫌な場合

dp = [[0, 0, 0] for _ in range(N+1)]

"""
    dp[i][0]: i日目にaを選んだときの最大値
    dp[i][1]: i日目にbを選んだときの最大値
    dp[i][2]: i日目にcを選んだときの最大値
"""

for i in range(N):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            if dp[i+1][j] < dp[i][k] + A[i][j]:
                dp[i+1][j] = dp[i][k] + A[i][j]

print(max(dp[N]))
