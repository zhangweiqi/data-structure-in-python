#!/usr/bin/env python
# coding:utf-8
"""
用类表示栈。
栈的方法都有：入栈，出栈，头，尾，求长度，求空。


用列表实现。
"""


class Stack(object):
    def __init(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack != []:
            self.stack.pop()
        else:
            return None

    def head(self):
        if self.stack != []:
            return self.stack[0]
        else:
            return None

    def tail(self):
        if self.stack != []:
            return self.stack[-1]
        else:
            return None

    def length(self):
        return len(self.stack)

    
    def empty(self):
        return self.stack == []
        """
        if self.stack == []:
            return True
        else:
            return False
        """

