def solution():
    n = int(input())

    a = [(0,0,0)]
    for _ in range(n):
        a.append(list(map(int,input().split())))
    print(a)
    """
     [[a0,b0,c0],...] 
        0日目のa,b,cの幸福度
    """

    dp=[[0,0,0]]*(n+1)
    print(len(dp))
    """
    dp[i][0]
    i日目にaを選んだときの幸福度の最大値
    dp[i][1]
    i日目にbを選んだときの幸福度の最大値
    dp[i][2]
    i日目にcを選んだときの幸福度の最大値
    """

    for i in range(1,n):
      for j in range(3):
          for k in range(3):
            if j==k: continue
            if dp[i+1][k]< dp[i][j]+a[i][k]:
                dp[i+1][k] = dp[i][j]+a[i][k]

    print(dp[n][0],dp[n][1],dp[n][2])
solution()