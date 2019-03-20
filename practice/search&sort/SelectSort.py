
def find_smallest(lyst):
    '''找到序列中的最小值并返回下标'''
    n = len(lyst)
    # if n < 1:
    #     return
    smallest = lyst[0]
    smallest_index = 0
    for i in range(1, n):
        if lyst[i] < smallest:
            smallest = lyst[i]
            smallest_index = i
    return smallest_index


def select_sort(lyst):
    '''选择排序'''
    sorted_lyst = []
    n = len(lyst)
    for i in range(n):
        small = find_smallest(lyst)
        sorted_lyst.append(lyst.pop(small))  # 将lyst中最小的元素弹出并添加到新列表中
    return sorted_lyst


if __name__ == '__main__':
    lyst = [1, 2, 5, 4, 3, 7, 6]
    res = select_sort(lyst)
    print(res)
