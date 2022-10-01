
def majorElement(nums):
    if not nums:
        return None
    if len(nums)==1:
        return nums[0]
    half=len(nums)//2
    a=majorElement(nums[:half])
    b=majorElement(nums[half:])

    return [b,a][nums.count(a)>half]


print(majorElement([2,2,1,1,1,2,2]))