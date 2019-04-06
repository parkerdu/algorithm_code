
def insert_sort(alist):
    """插入排序
        最优O(n)
        最差O(n**2)"""
    n = len(alist)
    for j in range(1, n):
        i = j
        while i:  # i=j,j-1,j-2,...,2,1 所以这里也可以用for i in range(j, 0 ,-1)
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break

li = [2,4,1,7,9,5,3]


print(li)
insert_sort(li)
print(li)
