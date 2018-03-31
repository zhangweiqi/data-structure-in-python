#!/usr/bin/env python
# coding:utf-8
"""
前序遍历：访问根节点的操作发生在遍历左右子树之前
中序遍历：访问根节点的操作发生在遍历左右子树之中
后序遍历：访问根节点的操作发生在遍历左右子树之后
"""

class Node(object):
    """
    节点类
    """

    def __init__(self, elem=0, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """
    树类
    """

    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        """
        添加节点
        :param elem:
        :return:
        """
        node = Node(elem)
        if self.root.elem == 0:
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]
            if treeNode.lchild == None:













    def front_recursion(self, root):
        """
        利用递归实现先序遍历
        :param root:
        :return:
        """
        if root == None:
            return None
        print root.elem
        self.front_recursion(root.lchild)
        self.front_recursion(root.rchild)

    def middle_recursion(self, root):
        """
        递归实现中序遍历
        :param root:
        :return:
        """
        if root == None:
            return None

