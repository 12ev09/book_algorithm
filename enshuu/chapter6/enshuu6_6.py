import sys, re
from math import ceil, floor, gamma, sin, sqrt, pi, factorial, gcd
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
整数A,B,Cが与えられる。
At + Bsin(Ctπ) = 100を満たす
0以上の実数tを10^-6以下の精度で1つ求める。
"""

def main():
    """
    t=0だと0 = 100　より満たさないので t > 0

    f(t) = At + Bsin(Ctπ)とすると
    f(t)-100の正負が入れ替わる瞬間はどこか?

    -中間値の定理-
    関数f(x)が閉区間[a,b]において連続で、f(a)≠f(b)ならば
    aとbの間の任意の実数kにおいて
    f(c) = k (a<c<b)
    を満たすような実数cが存在する。

    区間[a,b]の中でf(x)<100,f(x)>100を満たすようなxが存在したときに
    答えとなるようなcの範囲を狭めることができる

    """

    a,b,c = i_map()

    def f(t):
        s = b*sin(c*t*pi)
        return a*t + s

    alpha = float(0)
    beta = float(200)
    for _ in range(200):#区間幅が1/2^(100)になる
        gamma = (alpha+beta)/2
        if f(gamma) <=100: alpha =gamma
        else: beta = gamma
    
    print(beta)

if __name__ == '__main__':
    main()
