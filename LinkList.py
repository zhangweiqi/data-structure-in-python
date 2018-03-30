#!/usr/bin/python
# coding:utf-8
"""
链表：链表是由一个个结点构成的。
每个结点都由一个数值和一个指向下一个节点地址的指针构成。
因为指针指向的是下一个节点的地址，所以结点的地址都是随机的整数。
链表的表头为链表的头指针指向的地址。

该脚本使用 类的嵌套 实现链表。结点和链表都由类来表示。
结点有两个变量data和next，data存储数据，next为下一个结点。
链表有一个变量head，将node赋给head。

结点实现功能：创建结点（初始化）
链表实现功能：创建链表（初始化），插入结点，删除节点，查询结点，长度，是否为空，清空，删除。

"""


class Node(objec):
    def __init__(self, value, pointer=0):
        """
        用该类来表示结点，data为结点的值，next为下一个结点。
        data为int，next为类Node。

        初始化一个结点时，应该给出该结点的值。
        """
        self.data = value
        self.next = pointer



class LinkList(object):
    """
    用该类来表示链表，head为头结点，默认为0，赋予值之后为类Node。
    """
    def __init__(self):
        """
        初始化链表，head指针指向第一个结点。
        """
        self.head = 0


    def initlist(self, listdata):
        """
        用列表初始化链表，列表中的值为要加入链表的列表。
        """
        #将链表的head设为头结点
        self.head = Node(listdata[0])
        temp = self.head
        #循环嵌套
        for i in listdata[1:]:
            #初始化结点
            node = Node(i)
            #连接结点
            temp.next = node
            #修改循环变量
            temp = temp.next


    def length(self):
        """
        从head处查询链表的长度，向后查找，若哪个结点的next为0，则为最后一个结点。
        """
        p = self.head
        length = 0
        while p != 0:
            length += 1
            p = p.next
        return length


    def empty(self):
        """
        链表为空则返回True，否则为False。
        """
        if self.length() == 0:
            return True
        else:
            return False


    def clear(self):
        """
        清空链表
        """
        self.head = 0


    def append(self, item):
        # 定义新的结点
        new_node = Node(item)
        if self.head == 0:
            self.head = new_node
        else:
            # 从头开始找到最后一个结点，然后接上新结点
            temp = self.head
            while temp.next != 0:
                temp = temp.next
            temp.next = new_node


    def getitem(self, index):
        """
        得到index位置的结点
        """
        if self.empty():
            print 'LinkList is empty.'
            return None
        elif index < 0 or index >= self.length():
            print 'The index is out of the LinkList.'
            return None
        counter = 0
        temp = self.head
        while temp.next != 0 and counter < index:
            temp = temp.next
            counter += 1
        if counter == index:
            return temp.data
        else:
            print 'target is not exist!'


    def insert(self, index, item):
        """
        插入结点，item为数值。
        """
        if self.empty)():
            print 'LinkList is empty.'
            return None
        elif index > self.length():
            print 'The index is out of the LinkList.'
            return None
        if index == 0:
            self.head = Node(item, self.head)
            return None
        temp = self.head
        for i in range(index-1):
            temp = temp.next
            if temp.next == 0:
                temp.next = Node(item)
            else:
                old_item = temp.next
                temp.next = Node(item)
                temp.next.next = old_item
                return None


    def delete(self, index):
        """
        删除index位置的结点
        """
        if self.empty() or index < 0 or index >=self.length():
            print 'Index is out of the range'
            return None
        if index == 0:
            self.head = self.head.next
        temp = self.head
        for i in range(index-1):
            temp = temp.next
        if temp.next.next == 0:
            temp.next = 0
        else:
            temp.next = temp.next.next


    def index(self, value):
        """
        查询value在链表中的位置
        """
        if self.empty():
            print "LinkList is empty."
            return None
        temp = self.head
        counter = 0
        while temp.next != 0:
            if temp.data == value:
                return counter
            counter += 1
            temp = temp.next
        return 'No value!'

