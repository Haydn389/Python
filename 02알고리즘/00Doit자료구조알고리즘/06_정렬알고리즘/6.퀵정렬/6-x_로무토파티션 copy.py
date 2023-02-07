def quick_sort(arr, start, end):
    if start < end:
        pivot_index = lomuto_partition(arr, start, end)
        print("====left====")
        quick_sort(arr, start, pivot_index - 1) #pivot기준 왼쪽 sub_array에대해 반복
        print("====right====")
        quick_sort(arr, pivot_index + 1, end) #pivot기준 오른쪽 sub_array에대해 반복
cnt=0
def lomuto_partition(arr, start, end):
    print("----lomuto----")
    global cnt
    pivot = arr[end] #pivot 설정
    i = start - 1  
    for j in range(start, end): #피벗 전까지 j를 증가
        cnt+=1
        if arr[j] <= pivot: #pivot 보다 큰값을 찾기 전까지 i계속 증가
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            cnt+=1
            print(arr)
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    cnt+=1
    print(arr)
    return i + 1 #pivot의 인덱스를 반환 : pivot의 인덱스는 이후로 불변

arr = [1,4,3,7,8,6,5] #case 1
# arr = [1,2,3,4,5,6,7] #case 2 

quick_sort(arr, 0, len(arr) - 1)
print(arr)
print(cnt)
