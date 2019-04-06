# coding:utf-8


def quick_sort(alist, first, last):
    """快速排序"""
    if first >= last:
        return
    mid_value = alist[first]  # 要定位的值
    low = first  # 左游标
    high = last  # 右游标
    while low < high:
        #  第一步让high从右往左走
        while high > low and alist[high] >= mid_value:  # =号只放一个下面不放，实现和中间值相等的数都放在右边
            high -= 1  # 退出循环就表示high走到了<=中间值的一个人面前
        alist[low] = alist[high]
        #  第二步high被复制后让low往右走
        while low < high and alist[low] < mid_value:
            low += 1  # 退出循环表示low走到大于等于中间值那
        alist[high] = alist[low]
        # 第三部low被复制后转第一步
    # 循环退出 low=high= 中间该在的位置
    alist[low] = mid_value

    quick_sort(alist, first, low-1)  # 对mid_value左边递归调用函数
    quick_sort(alist, low+1, last)  # 对mid_value右边边递归调用函数

if __name__ == "__main__":
    a = [1, 5, 7, 8, 2, 4]
    print(a)
    quick_sort(a, 0, len(a)-1)
    print(a)
