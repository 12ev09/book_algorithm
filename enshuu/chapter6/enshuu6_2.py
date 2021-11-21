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
n要素からなる3つの整数列a,b,c
a_i < b_j < c_k
を満たすような i,j,kの組は幾つ存在するか(O(Nlog(N)))
"""



def main():
    """
    *方針*
    全探索だとO(N^3)で間に合わない
    二分探索を行うにしてもaを固定して繰り返す場合は
    O(log(n))回の操作をO(log(n))回やることになる
    O(n(log(n))^2)になってしまう

    bの要素b_iについて以下を繰り返す(O(n))
        (1) O(log(n))
        b_iが整数列aに挿入したとき何番目にあたるかを二分探索で求める.
        3番目に挿入できるならb_iより小さい値が3つあるということなので、3をcount_bに代入
        (2)o(log(n))
        cについても(1)と同様に行う
        (3)O(1)
        (1)と(2)で求めた値を掛けて、ansに加算

    計算量はO(nlog(n))
    """
    
    n = i_input()
    a,b,c = i_list(),i_list(),i_list()
    a.sort()
    b.sort()
    c.sort()

    ans =0

    for i in b:
        ans += bisect_left(a,i) * (n-bisect_right(c,i))

    print(ans)

if __name__ == '__main__':
    main()
