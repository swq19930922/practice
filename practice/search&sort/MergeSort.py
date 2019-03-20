
def merge_sort(lyst):
    '''归并排序'''
    if len(lyst) < 2:                   # 列表中只有一个元素时终止递归并返回列表
        return lyst
    mid = len(lyst)//2
    left = merge_sort(lyst[:mid])       # 左表
    right = merge_sort(lyst[mid:])      # 右表
    sorted_lyst = []                    # 新建空列表用于存放排序结果
    left_pointer, right_pointer = 0, 0
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] <= right[right_pointer]:
            sorted_lyst.append(left[left_pointer])
            left_pointer += 1
        else:
            sorted_lyst.append(right[right_pointer])
            right_pointer += 1
    sorted_lyst += left[left_pointer:]          # 添加左边剩余的元素
    sorted_lyst += right[right_pointer:]        # 添加右边剩余的元素
    return sorted_lyst


if __name__ =='__main__':
    lyst = [5, 2, 4, 3, 1]
    res = merge_sort(lyst)
    print(res)