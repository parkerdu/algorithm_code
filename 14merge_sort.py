# coding:utf-8

def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    # 当分到只剩一个元素时返回他
    if n<=1:
        return alist
    mid = n // 2
    # left采用归并后返回的有序新列表
    left_li = merge_sort(alist[:mid])

    # left采用归并后返回的有序新列表

    right_li = merge_sort(alist[mid:])

    # 只有在分到只剩一个元素的时候才会执行下面步骤，因为在n->n/2时候你递归调用，
    # 并不会给你left_li返回任何东西，你又进去递归调用n/2->n/4，又调用，知道n<=1返回东西了，才会执行下面的代码
    # 将两个有序子序列合并
    left_poniter, right_pointer = 0, 0
    merge_list = []
    while left_poniter<len(left_li) and right_pointer<len(right_li):
        if left_li[left_poniter] < right_li[right_pointer]:
            merge_list.append(left_li[left_poniter])
            left_poniter += 1
        elif left_li[left_poniter] > right_li[right_pointer]:
            merge_list.append(right_li[right_pointer])
            right_pointer += 1
    # 只要某个指针走到对应列表的最后一个元素，while 就会退出来，这时候要把另一个列表剩下元素追加上来
    merge_list += left_li[left_poniter:]
    merge_list += right_li[right_pointer:]
    return merge_list

if __name__ == "__main__":
    a = [1, 5, 7, 8, 2, 4]
    print(a)
    merge_sort(a)
    # 这里你会发现a并没有改变，因为归并排序跟之前几种排序方法不同，之前都是在原列表上操作，现在在新列表上操作，同时也返回一个有序的新列表
    print(a)
    print(merge_sort(a))