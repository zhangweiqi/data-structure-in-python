#!/usr/bin/python
# coding:utf-8
"""
������������һ������㹹�ɵġ�
ÿ����㶼��һ����ֵ��һ��ָ����һ���ڵ��ַ��ָ�빹�ɡ�
��Ϊָ��ָ�������һ���ڵ�ĵ�ַ�����Խ��ĵ�ַ���������������
����ı�ͷΪ�����ͷָ��ָ��ĵ�ַ��

�ýű�ʹ�� ���Ƕ�� ʵ����������������������ʾ��
�������������data��next��data�洢���ݣ�nextΪ��һ����㡣
������һ������head����node����head��

���ʵ�ֹ��ܣ�������㣨��ʼ����
����ʵ�ֹ��ܣ�����������ʼ�����������㣬ɾ���ڵ㣬��ѯ��㣬���ȣ��Ƿ�Ϊ�գ���գ�ɾ����

"""


class Node(objec):
    def __init__(self, value, pointer=0):
        """
        �ø�������ʾ��㣬dataΪ����ֵ��nextΪ��һ����㡣
        dataΪint��nextΪ��Node��

        ��ʼ��һ�����ʱ��Ӧ�ø����ý���ֵ��
        """
        self.data = value
        self.next = pointer


class LinkList(object):
    """
    �ø�������ʾ����headΪͷ��㣬Ĭ��Ϊ0������ֵ֮��Ϊ��Node��
    """

    def __init__(self):
        """
        ��ʼ������headָ��ָ���һ����㡣
        """
        self.head = 0

    def initlist(self, listdata):
        """
        ���б��ʼ�������б��е�ֵΪҪ����������б�
        """
        # �������head��Ϊͷ���
        self.head = Node(listdata[0])
        temp = self.head
        # ѭ��Ƕ��
        for i in listdata[1:]:
            # ��ʼ�����
            node = Node(i)
            # ���ӽ��
            temp.next = node
            # �޸�ѭ������
            temp = temp.next

    def length(self):
        """
        ��head����ѯ����ĳ��ȣ������ң����ĸ�����nextΪ0����Ϊ���һ����㡣
        """
        p = self.head
        length = 0
        while p != 0:
            length += 1
            p = p.next
        return length

    def empty(self):
        """
        ����Ϊ���򷵻�True������ΪFalse��
        """
        if self.length() == 0:
            return True
        else:
            return False

    def clear(self):
        """
        �������
        """
        self.head = 0

    def append(self, item):
        # �����µĽ��
        new_node = Node(item)
        if self.head == 0:
            self.head = new_node
        else:
            # ��ͷ��ʼ�ҵ����һ����㣬Ȼ������½��
            temp = self.head
            while temp.next != 0:
                temp = temp.next
            temp.next = new_node

    def getitem(self, index):
        """
        �õ�indexλ�õĽ��
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
        �����㣬itemΪ��ֵ��
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
    for i in range(index - 1):
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
    ɾ��indexλ�õĽ��
    """
    if self.empty() or index < 0 or index >= self.length():
        print 'Index is out of the range'
        return None
    if index == 0:
        self.head = self.head.next
    temp = self.head
    for i in range(index - 1):
        temp = temp.next
    if temp.next.next == 0:
        temp.next = 0
    else:
        temp.next = temp.next.next


def index(self, value):
    """
    ��ѯvalue�������е�λ��
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
