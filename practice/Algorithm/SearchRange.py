

def search_range(nums, target):
    '''在有序数组中查找目标值的第一个和最后一个位置，若无返回[-1,-1]'''
    lyst = []
    lenth = len(nums)
    left = 0
    right = lenth - 1
    # 记录第一次找到的目标值
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            lyst.append(mid)
            break
    # 沿着第一次找到的目标值往左右两边找
    if lyst:
        i, j = mid, mid
        while i > 0 and nums[i - 1] == nums[mid]:
            lyst.append(i - 1)
            i -= 1
        while j < lenth - 1 and nums[j + 1] == nums[mid]:
            lyst.append(j + 1)
            j += 1
        return [i, j]
    else:
        return [-1, -1]


if __name__ =='__main__':
    nums = [5,5,6,6,7,8,8]
    target = 6
    res = search_range(nums,target)
    print(res)