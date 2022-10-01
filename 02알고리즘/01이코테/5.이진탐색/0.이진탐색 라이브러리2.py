from bisect import bisect_left, bisect_right

a=[1,2,3,3,3,3,4,4,8,9]
def count_by_range(a,l_val,r_val):
    r_idx=bisect_right(a,r_val)
    l_idx=bisect_left(a,l_val)
    return r_idx-l_idx

#값이 4인 데이터 갯수 출력
print(count_by_range(a,4,4))

#값이 [-1,3]범이에 있는 데이터 갯수 출력
print(count_by_range(a,-1,3))
