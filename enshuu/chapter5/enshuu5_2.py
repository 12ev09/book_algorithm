"""
n個の整数をいくつか足し合わせて、Wと一致させられるかを判定する
"""

def check_sum():
    n,w= map(int,input().split())

    a = list(map(int,input().split()))

    """
    dp[i][j] :最初のiこの整数からいくつか選んだ整数の和がjかどうかをを表すブール変数

    dp[i+1][j]の値を考えるとき、a[i]を選ぶか選ばないで場合分けする

    a[i]を選ばない　→ dp[i][j]がtrueならa[i+1][j]はtrueになる(和がへんかしないので)

    a[i]を選ぶ　　　→ j => a[i] かつ dp[i][j-a[i]]がtrue　なら true

    """

    dp = [[False]*(w+1)]*(n+1)
    dp[0][0]=True

    for i in range(n):
        for j in range(1,w+1):
            if dp[i][j]: dp[i+1][j] =True
            if j >= a[i] and dp[i][j-a[i]]:dp[i+1][j] = True
                
    if dp[n][w]: print("Yes")
    else: print("No")

check_sum()