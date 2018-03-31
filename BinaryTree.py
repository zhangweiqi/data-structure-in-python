#!/usr/bin/env python
# coding:utf-8
"""
一、前序遍历：访问根节点的操作发生在遍历左右子树之前
    1、从根节点开始
    2、先访问父节点，再访问左子节点，再访问右子节点
    3、若子节点为空，则访问下一个节点
二、中序遍历：访问根节点的操作发生在遍历左右子树之中
    1、从根节点开始
    2、先访问左子节点，再访问父节点，再访问右子节点
    3、若某节点存在左子节点，就要一路找下去，
      直到找到某节点的左子节点为空
三、后序遍历：访问根节点的操作发生在遍历左右子树之后
"""


class Node(object):
    """
    节点类
    """

    def __init__(self, value=None, lchild=None, rchild=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """
    树类
    """

    def __init__(self):
        self.root = Node()
        self.myQueue = []

    '''
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
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)
    '''

    def front_recursion(self, root):
        """
        利用递归实现先序遍历
        :param root:
        :return:
        """
        if root.value == None:
            return None
        print root.value
        self.front_recursion(root.lchild)
        self.front_recursion(root.rchild)

    def middle_recursion(self, root):
        """
        递归实现中序遍历
        :param root:
        :return:
        """
        if root.value == None:
            return None
        self.middle_recursion(root.lchild)
        print root.value
        self.middle_recursion(root.rchild)


    def later_recursion(self, root):
        """
        递归实现后序遍历
        :param root:
        :return:
        """
        if root.value == None:
            return None
        self.later_recursion(root.lchild)
        self.later_recursion(root.rchild)
        print root.value

    def front_stack(self, root):
        """
        堆栈实现前序遍历
        :param root:
        :return:
        """
        if root.value == None:
            return None
        myStack = []
        node = root
        while node or myStack:
            while node:
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()
            print node.value








    def middle_stack(self, root):
        pass

    def later_stack(self, root):
        pass

    def level_queue(self, root):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
