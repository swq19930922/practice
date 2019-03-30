

def len_of_longest_substr(strs):
    '''最长不重复子串'''
    lenth = len(strs)
    max_len = 0
    dict1 = {}          # 存储strs中的字符，值为字符下标
    left = 0            # 指示重复字符首次出现位置的下一位
    i = 0
    while i < lenth:
        if strs[i] not in dict1:         # 添加未出现的字符到字典中
            dict1[strs[i]] = i
        else:
            left = max(left, dict1[strs[i]] + 1)
            dict1[strs[i]] = i
        max_len = max(max_len, i - left + 1)
        i += 1
    return max_len

strs = 'abba'
print(len_of_longest_substr(strs))