# coding:utf-8


class Queue(object):
    """队列"""
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """入队O(1)"""
        self.__list.append(item)
        # self.__list.insert(0)  # O(n)
    def dequeue(self):
        """出队O(n)"""
        return self.__list.pop(0)
        # return self.__list.pop # O(1)

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)


if __name__ == "__main__":
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
