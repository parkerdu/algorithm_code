
class Node(object):
    """把一个元素构造成节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleLinkList(object):
    """单向循环链表"""

    def __init__(self, node=None):
        self.__head = node  # __head表示私有变量 只在这个类中使用，不对外暴漏
        if node:
            node.next = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None  # 头指向空就是第一个节点没有，那就是空

    def length(self):
        """链表长度"""
        if self.is_empty():  # 空链表
            return 0
        # cur游标用来移动遍历节点
        cur = self.__head  # 起点在第一个节点
        # count记录数量
        count = 1
        while cur.next != self.__head:  # 这里不能用cur == self.__head 因为刚开始就是这个，所以cur最后走到最后一个节点停下
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        # cur游标用来移动遍历节点
        if self.is_empty():
            return
        cur = self.__head  # 起点在第一个节点
        while cur.next != self.__head:  # 是最后一个节点
            print(cur.elem, end=' ')  # 后面end为了不要让他换行
            cur = cur.next
        print(cur.elem)  # 当cur指向尾节点退出循环，未打印

    def add(self, item):
        """链表头部添加元素"，头插法
           由于单向循环链表要把尾节点指向新加的节点，所以要遍历找到尾节点
           时间复杂度增加为O（n)了"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            # 第一步找到尾节点
            while cur.next != self.__head:
                cur = cur.next
            # 循环完成cur指向尾节点了
            # 第二部把node新节点挂到原链表上第一个节点
            node.next = self.__head
            # 第三把头指向新节点
            self.__head = node
            # 第四把尾节点指向第一个node节点
            cur.next = node

    def append(self, item):
        """链表尾部添加元素,尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head  # 空列表时 cur == none 他没有next运行while就会出错
            while cur.next != self.__head:  # 当cur指向最后一个节点的元素时停止，不让他到最后一个节点的连接
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, pos, item):
        """指定位置添加元素
        :param pos 从0开始"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            node = Node(item)
            pre = self.__head  # pre最终走到pos-1位置，就是插入进去后的前一个位置
            for i in range(pos-1):  # pre要走pos-1次
                pre = pre.next
            # count = 0
            # while count != pos-1:  # 也是控制走pos-1次
            #     count += 1
            #     pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除找到的第一个item节点
            1.空列表
            2.删第一个
                2.1只有一个
                2.2不止一个
            3删中间及尾部"""
        pre = self.__head  # pre最后走到要删元素的前一个节点
        if pre.elem == item:  # 2特殊情况要删的是第一个元素
            if pre.next == self.__head:  # 2.1要删第一个且只有一个节点
                self.__head = None
            else:  # 2.2要删第一个不止一个
                # 由于是循环的，要把尾节点找到
                last = self.__head
                # 第一部找到尾节点
                while last.next != self.__head:
                    last = last.next
                # 第二部把头指向第二个节点
                self.__head = pre.next
                # 第三部 尾节点指向头节点
                last.next = self.__head
        elif pre == None:  # 1特殊情况空列表
            return
        else:  # 3删中间以及最后一个节点
            while pre.next != self.__head:  # 当pre走到倒数第二个节点也可删掉最后一个
                if pre.next.elem == item:  # pre.next = 当前要删的节点
                    pre.next = pre.next.next
                    return
                else:
                    pre = pre.next

    def search(self, item):
        """查找结点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        return False

if __name__ == "__main__":
    ll = SingleCycleLinkList()

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

