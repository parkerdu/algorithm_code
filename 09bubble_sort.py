# coding:utf-8


# def bubble_sort(alist):
#     """我的代码冒泡排序
#        始终都会以O(n**2)运行"""
#     length = len(alist)
#     while length - 1:  # 控制走n-1次  
#         for i in range(length - 1):  # 整个for 控制走完一次
#             if alist[i] > alist[i + 1]:
#                 mid = alist[i]
#                 alist[i] = alist[i + 1]
#                 alist[i + 1] = mid
#         length = length - 1


def bubble_sort(alist):
    """老师代码
        优化时间复杂度，最快可以达到O(n)"""
    n = len(alist)
    for j in range(n-1):  # 控制走n-1次
        for i in range(n-1-j):  # 整个for 控制走完一次
            count = 0
            if alist[i] > alist[i + 1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]  # 边走边实现交换
                count += 1
            if count == 0:  # 只要有一次走完没有交换就可以判定已经排好了
                return



li = [2,4,1,7,9,5,3]


print(li)
bubble_sort(li)
print(li)


