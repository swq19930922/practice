

def draw_repeat(strs):
    '''字符串去重，修改多少次可以使相邻字符不重复'''
    lenth = len(strs)
    count = 0
    swap = False            # 默认未修改
    i = 1
    while i < lenth:
        if strs[i] == strs[i-1] and not swap:   # 若与前一个元素相等且未修改，则计数加1，swap = True
            count += 1
            swap = True
        else:
            swap = False
            if strs[i] == strs[i-1] and swap:     # 若与前一个元素相同但已修改，则跳过该元素
                i += 1
        i += 1
    return count


if __name__ == '__main__':
    strs = 'aaaaabbcccdabbccc'
    s = draw_repeat(strs)
    print(s)
