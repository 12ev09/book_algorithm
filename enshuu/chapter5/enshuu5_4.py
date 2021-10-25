def main():
    n, w = map(int,input().split())
    a = list(map(int,input().split()))
    k= int(input())


    """
    O(NWK)での実装

    dp[i][j][k]: 最初からi個の整数からいくつか選んだ和がjに一致するかどうかを表すbool変数(但しi<=k)
    
    a[i]を選ばない場合
    dp[i][j][k]=trueならば
    dp[i+1][j][k] = true

    a[i]を選ぶ場合
    dp[i][j-a[i]][k-1]=true　かつ j>=a[i] かつ k >=1ならば
    dp[i+1][j][k] = true    
    """


    """
    O(NW)で実装するには

    dp[i][j]:最初からi個の整数からいくつか選んだ和がjに一致するような方法のうち、選ぶ整数の個数が最小のもの


    a[i]を選ばない場合
    dp[i+1][j] = min(dp[i+1][j],dp[i][j])

    a[i]を選ぶ場合
    j >= a[i]ならば
    dp[i+1][j] = min(dp[i+1][j],dp[i][j-a[i]]+1)

    dp[i][j]がk以下ならばYes、違えばNo


    Pythonにもchmin,chmaxが欲しい...(作ろう)
    """

    dp = [[0]*(w+1)]*(n+1)
    dp[0][0] = 0

    for i in range(n):
        for j in range(w):
            #a[i]を選ばない場合
            dp[i+1][j] = min(dp[i+1][j],dp[i][j])

            #a[i]を選ぶ場合
            if j >= a[i]:
                dp[i+1][j] = min(dp[i+1][j],dp[i][j-a[i]])

    if dp[n][w] <= k: print("Yes")
    else: print("No")

if __name__ == '__main__':
    main()

