# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

node_all = []

class node(object):
    # 节点个数
    node_num = 0

    # 初始函数
    def __init__(self,left_node,right_node,val):
        # 左节点
        self.left_node = left_node
        # 右节点
        self.right_node = right_node
        # 当前节点值
        self.val = val
        node.node_num += 1

    # 放入左节点
    def put_left_node(self,node):
        if self.left_node == None:
            self.left_node = node

    # 放入右节点
    def put_right_node(self, node):
        if self.right_node == None:
            self.right_node = node


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

# 输出二叉树
def print_tree(root):
    # 前序输出
    if node_all:
        # 根的深度
        dep = maxdepth(root_node)
        space = '  '
        for index,item in enumerate(node_all):
            if index%3 == 0:
                print str(space * dep) + str(item)
            elif index%3 == 1:
                print '/'
                print str(space * (dep - 1)) + str(item),
            elif index%3 == 2:
                print '\\',
                print str(space * (dep + 1)) + str(item),

# 反转二叉树


if __name__ == '__main__':
    # 新建一个左节点
    left_node_1 = node(None,None,2)
    left_node_2 = node(None, None, 4)
    left_node_3 = node(None, None, 6)

    # 新建一个右节点
    right_node_1 = node(None,None,1)
    right_node_2 = node(None, None, 3)
    right_node_3 = node(None, None, 5)
    # 新建根节点
    root_node = node(None,None,0)


    # 放入节点

    left_node_1.put_left_node(left_node_2)
    left_node_1.put_right_node(right_node_2)


    right_node_1.put_left_node(left_node_3)
    right_node_1.put_right_node(right_node_3)

    root_node.put_left_node(left_node_1)
    root_node.put_right_node(right_node_1)

    # node_all[0] = root_node.val
    # print_tree_all(root_node,0,0)

    # graorder(root_node)
    #dep = maxdepth(root_node)
    #print str(dep)
    # preorder(root_node)
    # print_tree(root_node)
    root_node = inverTree(root_node)

    print '1'

