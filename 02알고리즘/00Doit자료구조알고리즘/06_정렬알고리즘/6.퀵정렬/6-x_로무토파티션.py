input = [1,4,3,7,8,6,5] #case 1
# input = [1,2,3,4,5,6,7] #case 2 
cnt=0
def QuickSort(input):
    global cnt
    # 길이가 1 이하 일 경우 그대로 return
    if len(input)<=1:
        return input
    # pivot은 항상 수열의 오른쪽 끝 값
    pivot = input[len(input)-1]
    # left_pointer는 항상 수열의 왼쪽 첫 값
    left = 0        

    # right_pointer는 왼쪽에서 오른쪽으로 한칸씩 이동
    for right in range(len(input)):
        cnt+=1
        #right_pointer < pivot 일 경우 데이터 스왑
        if input[right] < pivot:
            input[right], input[left] = input[left], input[right]
            left += 1
            # cnt+=1
    # 마지막으로 left_pointer와 pivot 데이터 스왑
    input[len(input)-1], input[left] = input[left], input[len(input)-1]
    cnt+=1
    
    # 이동한 pivot의 위치를 기준으로 left_side, right_side 나누어 재귀
    left_side = QuickSort(input[:left])
    right_side = QuickSort(input[left:])
    
    # 받아온 정렬된 데이터들을 통합
    return left_side+right_side

print(QuickSort(input))
print(cnt) #case 1 : 