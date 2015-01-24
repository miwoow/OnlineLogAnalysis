#!/bin/python
#coding:utf-8

from Task import Task


class TaskQueue():
    '''
    任务队列
    '''
    queue = []

    def __init__(self,):
        pass

    def add(self, task):
        self.queue.append(task)
        return True

    def pop(self, ):
        try:
            return self.queue.pop()
        except IndexError, ex:
            return None


if __name__ == '__main__':
    tq = TaskQueue()
