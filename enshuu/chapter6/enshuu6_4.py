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
INF = 10 ** 7 
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
n個の0以上の実数かm個選んで、m個のうちの2つのくみの差の最小値として考えられる最大値
"""

def main():
    """
    -方針-

    最小値の最大化 => M個から任意に2つ選んだとき、距離がx以上になるか?
    ↑このxの最大値を二分探索で求める

    """

    n,m = i_map()
    a = i_list()
    a.sort()

    #xの候補を二分探索で絞っていくことを考える
    left = 0
    right = INF #無理な値を設定

    while(right - left > 1):
        x = (left+right)//2
        #全ての間隔をx以上にしてM個の小屋をとれるか?
        cnt = 1 # 何個とれたか
        prev = 0 # 初期状態
        for i in range(n):
            if a[i] - a[prev] >=x:
                cnt +=1
                prev = i
        #満たす場合は left <-x 満たさない場合は right <-x    
        if cnt >=m: left = x # まだxが大きくなるかも
        else: right = x      # xが大きすぎるので小さくする必要がありそう
    
    print(left)

if __name__ == '__main__':
    main()
