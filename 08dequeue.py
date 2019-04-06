# coding:utf-8


class Deque(object):
    """双端队列"""

    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """头部添加"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """尾部添加"""
        self.__list.append(item)

    def pop_front(self):
        """头部出队"""
        return self.__list.pop(0)

    def pop_rear(self):
        """尾部出队"""
        return self.__list.pop()

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)