"""
给定一个二叉树，请生成一个新的二叉树，使得新树中的每个节点的值等于原始树中该节点的左子树和右子树所有节点值的和。左子树表示该节点左侧叶子节点为根节点的一颗新树；右子树表示该节点右侧叶子节点为根节点的一颗新树。

原始二叉树：
 6
   / \
  7   9
 /   / \
-2  6   -7

生成的新二叉树：
20
   /  \
  -2   8
 /    / \
0    0   0
解释：

根节点 6 变为 20，因为它的左子树和右子树所有节点值的和为 7 + (-2) + 9 + 6 + (-7) = 20。
左子节点 7 变为 -2，因为它只有一个左子节点，值为 -2。
右子节点 9 变为 8，因为它的左右子节点值的和为 6 + (-7) = -1。
所有叶子节点变为 0，因为它们没有子节点。


作者：程序员基德
链接：https://www.nowcoder.com/discuss/694858938491084800?sourceSSR=users
来源：牛客网

题解：
这道题目的核心在于理解二叉树的遍历特性和如何利用中序遍历和前序遍历重建二叉树。解题步骤如下：

首先，需要根据给定的中序遍历和前序遍历序列重建原始二叉树。这是因为只有重建出原始树的结构，才能正确计算每个节点的子树和。

重建二叉树的关键在于理解前序遍历和中序遍历的特点：

前序遍历的第一个元素总是树的根节点。
在中序遍历中，根节点左边的元素属于左子树，右边的元素属于右子树。
利用这些特点，可以递归地重建二叉树：

从前序遍历中取第一个元素作为当前子树的根。
在中序遍历中找到这个根元素，将序列分为左右两部分。
递归地处理左右子树。
在重建树的过程中，同时计算每个节点的子树和。这可以通过在节点结构中添加一个额外的字段来实现。

最后，对重建并计算好子树和的树进行中序遍历，输出结果。

"""

# code
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 节点值
        self.left = left  # 左子节点
        self.right = right  # 右子节点
        self.child_sum = 0  # 子树和


def build_tree(inorder, preorder):
    if not inorder or not preorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)
    root_index = inorder.index(root_val)

    # 分割中序遍历
    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]

    # 分割前序遍历
    left_preorder = preorder[1:1 + len(left_inorder)]
    right_preorder = preorder[1 + len(left_inorder):]

    # 递归构建左右子树
    root.left = build_tree(left_inorder, left_preorder)
    root.right = build_tree(right_inorder, right_preorder)

    # 计算子树和
    root.child_sum = sum(left_inorder) + sum(right_inorder)

    return root


def get_mid_order(root):
    if not root:
        return []
    # 中序遍历：左 -> 根 -> 右
    return get_mid_order(root.left) + [root.child_sum] + get_mid_order(root.right)


# 读取输入
inorder = list(map(int, input().split()))
preorder = list(map(int, input().split()))

# 构建树并获取结果
root = build_tree(inorder, preorder)
result = get_mid_order(root)

# 输出结果
print(' '.join(map(str, result)))

