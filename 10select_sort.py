# coding:utf-8


def select_sort(alist):
    """我的代码,选择排序
       始终都会以O(n**2)运行"""
    n = len(alist)
    for j in range(n-1):  # 班长走n-1次 从0到n-2
        min_index = j  # 第几次走，就先认为第几个下标对应的是最小值
        for i in range(j+1, n):  # 每次走完确定最小值的下标 第j次走从第j+1个数开始比,一直比到最后一个人n-1
            if alist[i] < alist[min_index]:
                min_index = i
        alist[j],alist[min_index] = alist[min_index],alist[j]  # 走完交换







# def bubble_sort(alist):
#     """老师代码
#         优化时间复杂度，最快可以达到O(n)"""
#     n = len(alist)
#     for j in range(n-1):  # 控制走n-1次
#         for i in range(n-1-j):  # 整个for 控制走完一次
#             count = 0
#             if alist[i] > alist[i + 1]:
#                 # mid = alist[i]
#                 # alist[i] = alist[i + 1]
#                 # alist[i + 1] = mid
#                 alist[i], alist[i+1] = alist[i+1], alist[i]
#                 count += 1
#             if count == 0:  # 只要有一次走完没有交换就可以判定已经排好了
#                 return



li = [2,4,1,7,9,5,3]


print(li)
select_sort(li)
print(li)


