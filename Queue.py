#!/usr/bin/env python
# coding:utf-8

class Queue(object):
    #初始化队列
    def __init__(self):
        self.queue = []


    #入队
    def enqueue(self, item):
        self.queue.append(item)
    
    #出队
    def dequeue(self):
        if self.queue == []:
            return None
        else:
            return self.queue.pop(0)

    #得到头结点
    def head(self):
        if self.queue != []:
            return self.queue[0]
        else:
            return None

    #得到尾结点
    def tail(self):
        if self.queue != []:
            return self.queue[-1]
        else:
            return None

    #队列擦汗高难度
    def length(self):
        return len(self.queue)

    #验证是否为空
    def empty(self):
        return self.queue == []

