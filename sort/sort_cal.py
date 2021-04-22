# coding=utf-8

# 排序算法题

# 荷兰国旗:给定一个整数数组，给定一个值K，这个值在原数组中一定存在，
# 要求把数组中小于 K 的元素放到数组的左边，大于K的元素放到数组的右边，等于K的元素放到数组的中间，最终返回一个整数数组，其中只有两个值，分别是等于K的数组部分的左右两个下标值。


def sortColors(list):
    size = len(list)

    left = 0
    right = size - 1
    i = left
    while i <= right:
        if list[i] == 2:
            if list[right] != 2:
                list[i], list[right] = list[right], list[i]
                right = right - 1
        elif list[i] == 0:
            if list[right] != 0:
                list[i], list[left] = list[left], list[i]
                left = left + 1

        i += 1

    return list


if __name__ == '__main__':
    arr = [2, 0, 2, 1, 1, 0]
    sortColors(arr)
    for i in arr:
        print i
