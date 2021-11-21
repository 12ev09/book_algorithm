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
n要素からなる整数列それぞれについて、大きさが何番目かを求める。(計算量はnlog(n))

(例)
a = 12, 43, 7 ,15 ,9
ans:(2,4,0,3,1)

方針

 以下の処理をn回繰り返す(O(n))
 a_iが何番目かを二分探索で求める(O(log(n)))
"""



#ライブラリなし
def main1():
    n = i_input()
    a = i_list()

    # 二分探索のためにソートする
    a_copy = sorted(a)

    b = []

    for i in a:
        left=0
        right = n-1
        while right>=left:#対象となる要素数が0になるまで繰り返す
            mid = (right+left)//2
            if i == a_copy[mid]:
                b.append(mid)
                break
            elif i > a_copy[mid]:
                left = mid+1
            else:
                right = mid-1
    
    print(b)

#ライブラリあり
def main2():
    n = 5
    a = [13,43,7,15,9]
    print(a)
    a_copy = sorted(a)
    print(a_copy)
    a_copy.append(INF)
    b=[]

    for i in a:
        #iがa_copyの何番目
        b.append(bisect_left(a_copy,i))

    print(b)


if __name__ == '__main__':
    #main1()
    main2()
