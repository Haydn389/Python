import sys
from typing import Sequence
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def tree(a):
    n=len(a)  #a의 길이 저장
    if n<=1: #a가 리프노드에 도달하면 바로 반환
        return a
    for i in range(1,n): # 1부터 시작하는 이유: 0은 root이기 때문에 후위 순회에서는 마지막에 출력이라 빼줌.
        if a[0]<a[i]: #오른쪽 서브트리가 발견될 경우 분리시킴
            return tree(a[1:i])+tree(a[i:])+[a[0]]
    #오른쪽 서브트리가 발견이 되지 않을경우(왼쪽서브트리만있음)
    return tree(a[1:])+[a[0]]

a=[]

while True:
    try:
        a.append(int(input()))
    except:
        break

a=tree(a)
print(a)