#!/bin/python
#coding:utf-8

from TaskQueue import TaskQueue
import time


class TaskSchedule():
    '''
    任务调度类。
    '''
    normalQueue = TaskQueue()

    def __init__(self,):
        pass

    def run(self,):
        while True:
            task = self.normalQueue.pop()
            if task is not None:
                task.run()
            else:
                time.sleep(10)

if __name__ == '__main__':
    ts = TaskSchedule()
    ts.run()
