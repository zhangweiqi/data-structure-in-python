#!/usr/bin/env python
# coding:utf-8

class Queue(object):
    # ��ʼ������
    def __init__(self):
        self.queue = []

    # ���
    def enqueue(self, item):
        self.queue.append(item)

    # ����
    def dequeue(self):
        if self.queue == []:
            return None
        else:
            return self.queue.pop(0)

    # �õ�ͷ���
    def head(self):
        if self.queue != []:
            return self.queue[0]
        else:
            return None

    # �õ�β���
    def tail(self):
        if self.queue != []:
            return self.queue[-1]
        else:
            return None

    # ���в������Ѷ�
    def length(self):
        return len(self.queue)

    # ��֤�Ƿ�Ϊ��
    def empty(self):
        return self.queue == []
