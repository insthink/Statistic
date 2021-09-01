# author:insthink
# contact: insthink@qq.com
# datetime:21/8/29 上午11:38
# software: PyCharm

from collections import Counter
from math import sqrt


def frequency(data):
    """频率"""
    counter = Counter(data)
    return [(t[0], t[1] / len(data)) for t in counter.most_common()]


def mode(data):
    """众数"""
    # counter中的频数是从大到小排列的
    counter = Counter(data)

    # 没有众数的情况
    counter_tuple = counter.most_common()
    mode_cnt = counter_tuple[0][1]
    if mode_cnt == 1:
        return None, None

    ret = []
    for p in counter_tuple:
        # 频数从大到小遍历
        # 遇到小于众数的频数则停止
        if p[1] != mode_cnt:
            break
        ret.append(p[0])
    return ret, mode_cnt


def median(data):
    """中位数"""
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 1:
        return sorted_data[n // 2]
    return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2


def mean(data):
    """均值"""
    return sum(data) / len(data)


def rng(data):
    """极差"""
    return max(data) - min(data)


def quartile(data):
    """四分位数（将一组数通过3个点分成4份）"""
    n = len(data)
    q1, q2, q3 = None, None, None
    if n < 4:
        return q1, q2, q3

    q2 = median(data)
    sorted_data = sorted(data)
    if n % 2 == 1:
        q1 = median(sorted_data[:n // 2])
        q3 = median(sorted_data[n // 2 + 1:])
    else:
        q1 = median(sorted_data[: n // 2])
        q3 = median(sorted_data[n // 2:])

    return q1, q2, q3


def variance(data):
    """方差"""
    n = len(data)
    if n < 2:
        return None

    mean_val = mean(data)
    return sum((x - mean_val) ** 2 for x in data) / (n - 1)


def std(data):
    """标准差"""
    return sqrt(variance(data))