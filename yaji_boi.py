#encoding=utf=8
# 用递归的方法判断是否是回文字符串

def is_palindrome(str1=""):
    if str1 is None:
        return False
    # filter some special char
    str1 = ''.join(filter(str.isalnum, str1)).lower()
    str_len = len(str1)
    for index, sub_str in enumerate(str1[:int(str_len/2)]):
        if str1[index] != str1[str_len-index-1]:
            return False
        is_palindrome(str1[index:str_len-index-1])
    return True
