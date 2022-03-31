from bisect import bisect_right

"""
N要素からなる2つの正の整数列a,bこれら2つから
1個ずつ選んで積をとってできるN^2個の整数のうち、K番目に小さい値を求められるアルゴリズム
計算量は積の最大値をCとして、O(Nlog(N)log(C))
"""

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

N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort()


def check(x):
    """
        x以下の積がK個以上あるか
        """
    cnt = 0
    for a_i in a:
        # x/a_i 以下のものは何個あるか
        # 2つの添字を扱って和や積を求める場合、一方を固定して考えるのが定石
        cnt += bisect_right(b, x/a_i)

    if cnt >= K:
        return True

    return False


ok = 0
ng = 10**8

while ng-ok > 1:
    mid = (ok + ng) // 2

    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)
