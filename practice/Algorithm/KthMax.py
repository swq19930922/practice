

def partion(lyst, start, end):
    '''采用快排的思想将列表拆分，返回每次排序确定的元素的索引'''
    if start >= end:
        return start
    low = start
    high = end
    pivot = lyst[high]                              # 由于是确定第k大元素，采用倒序排列
    while low < high:
        while low < high and lyst[low] >= pivot:
            low += 1
        lyst[high] = lyst[low]
        while low < high and lyst[high] < pivot:
            high -= 1
        lyst[low] = lyst[high]
    lyst[high] = pivot
    return high                                     # 返回确定元素的索引


def kth_max(lyst, start, end, k):
    '''无序数组第k大值'''
    index = partion(lyst, start, end)               # 每次排序所确定元素的索引
    if index == k-1:                                # 索引从0开始，因此与k-1相比
        return lyst[index]
    elif index < k-1:
        return kth_max(lyst, index+1, end, k)       # k-1比索引大则需在lyst【index】右侧查找
    else:
        return kth_max(lyst, start, index-1, k)     # k-1比索引小则需在lyst【index】左侧查找


if __name__ == '__main__':
    lyst = [1,3,5,2,4,9,8]
    res = kth_max(lyst,0,len(lyst)-1, 2)
    print(res)