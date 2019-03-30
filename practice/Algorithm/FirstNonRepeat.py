

def first_non_repeat(string):
    '''第一个不重复字符'''
    n = len(string)
    char_count = {}
    for i in range(n):
        if string[i] in char_count:
            char_count[string[i]] += 1
        else:
            char_count[string[i]] = 1
    for i in range(n):
        if char_count[string[i]] == 1:
            return string[i]

string = 'aabcdeb'
print(first_non_repeat(string))