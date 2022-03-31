"""
文字列S,Tの最長共通部分列の長さを求める
例) 「ABCX」と「AYBZC」との最長共通部分列は「ABC」である
"""

"""
input
ABC
AYBZC

output
    3
"""

S = input()
T = input()

N = len(S)
M = len(T)

"""
dp[i][j] → 文字列 S の最初の i 文字と、文字列 T の最初の j 文字分との間の LCS の長さ
"""

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(N+1):
    for j in range(M+1):
        # Sのi文字目とTのj文字目が一致する場合
        if i > 0 and j > 0:
            if S[i-1] == T[j-1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
            else:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1])

        # Sに1文字追加
        dp[i][j] = max(dp[i][j], dp[i-1][j])

        # Tに1文字追加
        dp[i][j] = max(dp[i][j], dp[i][j-1])

print(dp[N][M])
