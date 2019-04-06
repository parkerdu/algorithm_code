
class Node(object):
    """把一个元素构造成节点"""
    def __init__(self, elem):
        self.elem = elem
        self.prev = None
        self.next = None


class DoubleLinkList(object):
    """双链表"""

    def __init__(self, node=None):
        self.__head = node  # __head表示私有变量 只在这个类中使用，不对外暴漏

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None  # 头指向空就是第一个节点没有，那就是空

    def length(self):
        """链表长度"""
        # cur游标用来移动遍历节点
        cur = self.__head  # 起点在第一个节点
        # count记录数量
        count = 0
        while cur != None:  # None是最后一个节点
            count += 1
            cur = cur.next
        return count
        # 知道cur == None 时结束

    def travel(self):
        """遍历链表"""
        # cur游标用来移动遍历节点
        cur = self.__head  # 起点在第一个节点
        while cur != None:  # None是最后一个节点
            print(cur.elem, end=' ')  # 后面end为了不要让他换行
            cur = cur.next
        # 知道cur == None 时结束
        print('')  # 用来换行

    def add(self, item):
        """链表头部添加元素"，头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self, item):
        """链表尾部添加元素,尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head  # 空列表时 cur == none 他没有next运行while就会出错
            while cur.next != None:  # 当cur指向最后一个节点的元素时停止，不让他到最后一个节点的连接
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """指定位置添加元素
        :param pos 从0开始"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head  # cur最终走到pos位置，就是插入进去的位置
            for i in range(pos):  # pre要走pos-1次
                cur = cur.next
            # count = 0
            # while count != pos-1:  # 也是控制走pos-1次
            #     count += 1
            #     pre = pre.next
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node


    def remove(self, item):
        """删除找到的第一个item节点"""
        cur = self.__head  # cur最后走到要删元素
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:  # 要删第一个节点
                    self.__head = cur.next
                    if cur.next:  # 为了保证只有一个节点时候不进行这操作
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:  # 保证删最后一个节点
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next


    def search(self, item):
        """查找结点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
if __name__ == "__main__":
    ll = DoubleLinkList()

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    ll.insert(-1,9)
    ll.insert(3, 100)
    ll.insert(29, 200)
    ll.travel()

    ll.remove(9)
    ll.travel()

    ll.remove(200)
    ll.travel()