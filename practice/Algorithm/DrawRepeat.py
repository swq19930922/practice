
# 在python3.7下编写,不明白系统如何测试


def draw_repeat(strs):
    lenth = len(strs)
    count = 0
    swap = False
    i=1
    while i < lenth:
        if strs[i] == strs[i-1] and not swap:
            count += 1
            swap = True
        elif strs[i] == strs[i-1] and swap:
            i += 1
            swap = False
        elif strs[i] != strs[i-1]:
            swap = False
        i += 1
    return count


if __name__ == '__main__':
    strs = 'aaaaabbcccdabbccc'
    s = draw_repeat(strs)
    print(s)
