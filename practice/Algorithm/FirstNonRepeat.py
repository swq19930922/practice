

def first_non_repeat(string):
    '''第一个不重复字符'''
    n = len(string)
    char_count = {}
    for i in range(n):
        if string[i] in char_count:         # 第i个字符每出现一次计数加1
            char_count[string[i]] += 1
        else:
            char_count[string[i]] = 1
    for i in range(n):
        if char_count[string[i]] == 1:      # 遍历字符串找到对应计数为1的字符
            return string[i]


if __name__ == '__main__':
    string = 'aabcdeb'
    print(first_non_repeat(string))
