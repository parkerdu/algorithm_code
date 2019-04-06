
def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n // 2  # n除以2取整 如9//2=4
    while gap:  # 控制gap下降到gap = 1
        for j in range(gap, n):  # 整个for循环完成对一次gap取值的排序
            i = j  # 总共要完成n-gap次比较交换 分别是i = gap,gap+1,gap+2,...,n-1
            while i:  # 整个while完成一次插入排序
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2
    # 下面是整个插入排序，可以看出当上面希尔排序的gap=1时候和下面的代码是一样的
    # for j in range(1, n):  # 整个for循环完成插入排序
    #     i = j
    #     while i:  # i=j,j-1,j-2,...,2,1 所以这里也可以用for i in range(j, 0 ,-1)
    #         if alist[i] < alist[i-1]:
    #             alist[i], alist[i-1] = alist[i-1], alist[i]
    #             i -= 1
    #         else:
    #             break
li = [2,4,1,7,9,5,3]


print(li)
shell_sort(li)
print(li)