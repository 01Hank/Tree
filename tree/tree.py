# coding=utf-8

class node(object):
    # 节点个数
    node_num = 0

    # 初始函数
    def __init__(self, left_node, right_node, val):
        # 左节点
        self.left_node = left_node
        # 右节点
        self.right_node = right_node
        # 当前节点值
        self.val = val
        node.node_num += 1

    # 放入左节点
    def put_left_node(self, node):
        if self.left_node == None:
            self.left_node = node

    # 放入右节点
    def put_right_node(self, node):
        if self.right_node == None:
            self.right_node = node
