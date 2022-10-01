import sys
sys.setrecursionlimit(10**8)  # 10^8 까지 늘림.
num = 8

sorted = [None]*num

def merge(a, m, middle, n):  # 시작점, 중간점, 끝점
    i = m
    j = middle+1
    k = m
    # 작은 순으로 배열에 삽입
    while (i <= middle and j <= n):
        if (a[i] <= a[j]):
            sorted[k] = a[i]
            i += 1
        else:
            sorted[k] = a[j]
        k += 1
    if (middle < i):
        for t in range(j, n+1):
            sorted[k] = a[t]
            k += 1
    else:
        for t in range(i, middle+1):
            sorted[k] = a[t]
            k += 1
    for t in range(m, n+1):
        a[t] = sorted[t]


def mergeSort(a, m, n):
    if (m < n):
        middle = (m+n)//2
        mergeSort(a, m, middle)
        mergeSort(a, middle+1, m)
        merge(a, m, middle, n)


if __name__ == "__main__":
    array = [7, 6, 5, 8, 3, 5, 9, 1]
    mergeSort(array, 0, len(array))
    print(array)
