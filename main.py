# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tree.tree import node
import tree.tree_op as op
import tree.frop_problem as frop

node_all = []


# 输出二叉树
def print_tree(root):
    # 前序输出
    if node_all:
        # 根的深度
        dep = op.maxdepth(root_node)
        space = '  '
        for index, item in enumerate(node_all):
            if index % 3 == 0:
                print str(space * dep) + str(item)
            elif index % 3 == 1:
                print '/'
                print str(space * (dep - 1)) + str(item),
            elif index % 3 == 2:
                print '\\',
                print str(space * (dep + 1)) + str(item),


if __name__ == '__main__':
    # 新建一个左节点
    left_node_1 = node(None, None, 2)
    left_node_2 = node(None, None, 4)
    left_node_3 = node(None, None, 6)

    # 新建一个右节点
    right_node_1 = node(None, None, 1)
    right_node_2 = node(None, None, 3)
    right_node_3 = node(None, None, 5)
    # 新建根节点
    root_node = node(None, None, 0)

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
    # dep = maxdepth(root_node)
    # print str(dep)
    op.preorder(root_node)
    node_all = op.node_all
    print_tree(root_node)
    # root_node = op.inverTree(root_node)

    print '1'
