
def binary_search(lyst, num):
    '''二分查找非递归实现'''
    left = 0
    right = len(lyst)-1
    while left < right:
        mid = (left + right)//2  # 中间位置下标
        if lyst[mid] == num:
            return mid           # 找到则返回下标
        elif lyst[mid] < num:
            left = mid + 1       # 若待查找项大于中间元素的值则查找右半部分
        else:
            right = mid - 1      # 若待查找项大于中间元素的值则查找左半部分
    return None


def binary_search_r(lyst, num):
    '''二分查找递归实现'''
    n = len(lyst) - 1
    if n < 0:
        return None
    mid = n//2
    if lyst[mid] == num:
        return mid                                  # 找到则返回下标
    elif lyst[mid] < num:
        return binary_search_r(lyst[mid+1:], num)   # 若待查找项大于中间元素的值则查找右半部分
    else:
        return binary_search_r(lyst[:mid], num)     # 若待查找项大于中间元素的值则查找左半部分


if __name__ == "__main__":
    lyst = [1, 3, 5, 6, 8, 9]
    num1 = 5
    num2 = 0
    res1 = binary_search(lyst, num1)
    res2 = binary_search_r(lyst, num1)
    res3 = binary_search(lyst, num2)
    res4 = binary_search_r(lyst, num2)
    print(res1)
print(res2)
print(res3)
print(res4)
