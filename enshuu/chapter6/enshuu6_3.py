import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
# input = sys.stdin.readline 
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []
def chmax(dp,i,j,x):
   if x> dp[i][j]:
       dp[i][j]=x
       return True
   return False
def chmin(dp,i,j,x):
   if x<dp[i][j]: 
       dp[i][j]=x
       return True
   return False

"""
n個の整数が与えられて、これらから重複を許して4個選んで総和を取った値のうち、Mを超えない範囲での最大値(N^2log(N))
1個も選ばなくても良い.
"""

def main():
    """
    方針

    選ぶ個数が1,2,3個でもよいというのがやっかいなので、n個の整数に0を加える。
    n個の整数から2個選んだときのその和を集めた集合Sを求める(O(N^2))

    Sから整数a,bをn個選んだときの和のMを超えない範囲での最大値を求める。(O(N^2log(N)))

    Sをsortする(N^2log(N))

    aを固定してSから整数を選んだときM-aを超えないような範囲での最大値を二分探索で求める(O(log(N))

    aを動かすNlog(N)

    計算量はO(N^2log(N))
    

    """

    _, m = i_map()
    a = i_list()
    a.append(0)

    s = []

    for i in a:
        for j in a:
            s.append(i+j)
    s.append(INF)
    s.sort()

    ans =0
    for i in s:
        #m-aが何番目に挿入できるかを求める。その一個手前の要素が条件を満たすなかでの最大値となる
        #上記の値+iが最大となるものを求める
        if m>=i: #ここ重要(2つ足し合わせたものがm以内におさまる保証はない)
            ans = max(ans,s[bisect_right(s,m-i)-1]+i)

    print(ans)

if __name__ == '__main__':
    main()
