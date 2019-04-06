# coding:utf-8


class Stack(object):
    """栈"""
    def __init__(self):
        self.__list = []

    def push(self, item):
        """压栈
        顺序表尾部操作时间复杂度为O(1)"""
        self.__list.append(item)

    def pop(self):
        """出栈"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素是啥，不出去"""
        if self.__list:  # 因为空列表没有-1
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        """判空"""
        return self.__list == []

    def size(self):
        """返回栈元素个数"""
        return len(self.__list)

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())