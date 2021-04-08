# coding=utf-8

# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

# 递归结果集，减少递归重复计算
result = {}

def numWays(n):
    if n == 0:
        return 1
    if n <= 2:
        return n

    # 先判断字典里面记录计算结果没有
    if n in result.keys():
        # 字典里面有，直接返回字典记录值
        return result[n]
    else:
        # 字典里面没有，计算以后放入值
        result[n] = numWays(n - 1) + numWays(n - 2)
        return result[n]


if __name__ == '__main__':
    num = numWays(5)
    print num