# coding=utf-8

node_all = []


# 树的最大深度
def maxdepth(root):
    if root is None:
        return 0
    return max(maxdepth(root.left_node),maxdepth(root.right_node)) + 1

# 前序遍历
def preorder(root):
    if root is None:
        print root.val
        return
    node_all.append(root.val)
    print root.val
    if root.left_node:
        preorder(root.left_node)
    if root.right_node:
        preorder(root.right_node)

# 中序遍历
def midorder(root):
    if root is None:
        print root.val
        return

    if root.left_node:
        preorder(root.left_node)
    print root.val
    if root.right_node:
        preorder(root.right_node)

# 后序遍历
def endorder(root):
    if root is None:
        print root.val
        return
    if root.left_node:
        endorder(root.left_node)
    if root.right_node:
        endorder(root.right_node)
    print root.val



# 广度遍历
def graorder(root):
       if root is None:
           print root.val
           return
       queue = [root]
       while queue:
           res = []
           for item in queue:
               # node_all.append(root.val)
               print item.val
               if item.left_node:
                   res.append(item.left_node)
               if item.right_node:
                   res.append(item.right_node)
               queue = res


# 比较两棵树是否相等
def issame(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 and root2:
        return root1.val == root2.val and issame(root1.left_node, root2.left_node) and issame(root1.right_node, root2.right_node)
    else:
        return False


# 反转树
def inverTree(root):
    if root is None or root.left_node is None or root.right_node is None:
        return root

    #反转左子树
    left_node = inverTree(root.left_node)
    # 反转右子树
    right_node = inverTree(root.right_node)

    #重新赋值
    root.left_node = right_node
    root.right_node = left_node
    return root
