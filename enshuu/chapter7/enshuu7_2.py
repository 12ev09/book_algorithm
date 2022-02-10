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
example input
3
2 4
5 7
3 8
4 7
5 10
1 9
"""

def main():
    n = i_input()
    red_points = []
    blue_points = []

    for _ in range(n):
        x,y = i_map()
        red_points.append((x,y))
         
    for _ in range(n):
        x,y = i_map()
        blue_points.append((x,y))
    
    red_points.sort()
    blue_points.sort()

    print(red_points)
    print(blue_points)

    #赤い点がマッチング済みかを示す配列
    used = [False] * n
    
    ans = 0
    #青い点をみる
    for i in range(n):

        maxy = 0
        maxid = -1
        # 使用済みでないかつ、y座標が最大の点を探す
        for j in range(n):
            if used[j]: continue

            if red_points[j][0] >= blue_points[i][0]:continue
            if red_points[j][1] >= blue_points[i][1]:continue

            #最大値を更新
            if (maxy < red_points[j][1]): 
                maxy = red_points[j][1]
                maxid =j

        if maxid==-1: 
            continue
        else:
            print(red_points[maxid],blue_points[i])
            ans +=1 
            used[maxid] = True

    print(ans)

if __name__ == '__main__':
    main()
