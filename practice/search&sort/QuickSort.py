
def quick_sort1(lyst):
    '''快速排序方法1'''
    if len(lyst) < 2:
        return lyst                             # 当列表元素少于两个默认有序，返回该列表
    pivot = lyst[0]                             # 基准值
    left = [x for x in lyst[1:] if x <= pivot]  # 将小于基准值的放在left列表
    right = [x for x in lyst[1:] if x > pivot]  # 将大于基准值的放在right列表
    return quick_sort1(left) + [pivot] + quick_sort1(right)


def quick_sort2(lyst, first, last):
    '''快速排序方法2'''
    if first > last:
        return
    low = first
    high = last
    pivot = lyst[first]
    while low < high:               # 控制low和high靠拢
        while low < high and lyst[high] >= pivot:
            high -= 1
        lyst[low] = lyst[high]      # 将大于基准值的放在左边
        while low < high and lyst[low] < pivot:
            low += 1
        lyst[high] = lyst[low]      # 将小于基准值的放在右边
    lyst[low] = pivot               # low与high相遇处即为基准值的位置
    quick_sort2(lyst, first, low-1)
    quick_sort2(lyst, low+1, last)
    return lyst


if __name__ == '__main__':
    lyst = [1, 3, 2, 5, 4, 7, 6]
    res1 = quick_sort1(lyst)
    res2 = quick_sort2(lyst, 0, 6)
    print(res1)
    print(res2)