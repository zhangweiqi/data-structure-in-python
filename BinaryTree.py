#!/usr/bin/env python
# coding:utf-8

class Node(object):
    """
    节点类
    """
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem=elem
        self.lchild=lchild
        self.rchild=rchild


class Tree(object):
    """
    树类
    """
    def __init__(self):
        self.root =Node()
        self.myQueue=[]


    def add(self, elem):
        """
        添加节点
        :param elem:
        :return:
        """
        node = Node(elem)

    def front_digui(self, root):
        """
        利用递归实现先序遍历
        :param root:
        :return:
        """
