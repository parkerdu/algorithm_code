# coding:utf-8

def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    mid = n // 2
    # left采用归并后返回的有序新列表
    left_li = merge_sort(alist[:mid])

    # left采用归并后返回的有序新列表

    right_li = merge_sort(alist[mid:])
    # 将两个有序子序列合并
    left_poniter, right_pointer = 0, 0

