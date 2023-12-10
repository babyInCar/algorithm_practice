from functools import cache


def find_longest_common_str(str1, str2):
    n = len(str1)
    m = len(str2)

    @cache
    def dfs(i, j):
        print(i,j)
        if i < 0 or j < 0:
            return 0
        if str1[i] == str2[j]:
            return dfs(str1[i - 1], str2[j - 1])
        print(dfs(i - 1, j))
        print(dfs(i, j - 1))
        return dfs(i - 1, j) if len(dfs(i - 1, j)) > len(dfs(i, j - 1)) else dfs(i, j - 1)

    return dfs(n - 1, m - 1)

str1 = "abcdefghijklmnop"
str2 = "abcsafjklmnopqrstuvw"
print(find_longest_common_str(str1, str2))