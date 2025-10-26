"""
部门组织绿岛骑行团建活动。租用公共双人自行车，每辆自行车最多坐两人，最大载重M。给出部门每个人的体重，请问最多需要租用多少双人自行车。

输入描述
第一行两个数字m、n，分别代表自行车限重，部门总人数。
第二行，n个数字，代表每个人的体重，体重都小于等于自行车限重m。

0<m<=200
0<n<=1000000
输出描述
最小需要的双人自行车数量。

用例1
输入
3 4
3 2 2 1

输出：
3
"""
def main():
    """计算"""
    bicycle_limit, people = list(map(int, input().split()))
    weight_list = list(map(int, input().split()))
    weight_list.sort()
    res = 0
    left = 0
    right = people - 1
    while left <= right:
        if weight_list[left] + weight_list[right] <= bicycle_limit:
            res += 1
            left +=1
            right -= 1
        else:
            # 题目限定体重一定是比限重小的，所以也要加上1
            right -= 1
            res += 1
    print(res)


if __name__ == '__main__':
    main()