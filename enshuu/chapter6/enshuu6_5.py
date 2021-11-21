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
N要素からなる2つの正の整数列a,bこれら2つから
1個ずつ選んで積をとってできるN^2個の整数のうち、K番目に小さい値を求められるアルゴリズム
計算量は積の最大値をCとして、O(Nlog(N)log(C))
"""

def main():
    """
    -方針-
    (1)
    全部の積を計算するとO(N^2)
    それをsortするとO(N^2log(N))
    →間に合わない →全部の積を計算しちゃいけない


    (2)
    x以下の積がK個以上あるかを判定する ...(*)
    (*)で二分探索
    """
    _,k = i_map()
    a = i_list()
    b = i_list()

    b.sort()

    
    def check(x):
        """
        x以下の積がK個以上あるか
        """    
        cnt = 0
        for a_i in a:
            # x/a_i 以下のものは何個あるか
            # 2つの添字を扱って和や積を求める場合、一方を固定して考えるのが定石
            cnt +=bisect_right(b,x/a_i)
        
        if cnt >=k: return True
        return False

    left = 0
    right =10**8

    #要素が1になるまで
    while(right - left >1):
        mid = (left+right)//2

        if(check(mid)): right = mid
        else: left = mid

    print(right)


if __name__ == '__main__':
    main()
