# author:insthink
# contact: insthink@qq.com
# datetime:21/9/2 下午11:08
# software: PyCharm

import random

import matplotlib.pyplot as plt

from playStats.descriptive_stats import *


def variance_bias(data):
    """有偏的样本方差"""
    n = len(data)
    if n < 2:
        return None

    mean_val = mean(data)
    return sum((x - mean_val) ** 2 for x in data) / n


def sample(num_of_samples, sample_sz, dt, var):
    data = []
    for _ in range(num_of_samples):
        data.append(var([dt.__call__() for _ in range(sample_sz)]))
    return data


if __name__ == '__main__':
    data1 = sample(10000, 40, lambda: random.uniform(0, 1), variance)
    plt.hist(data1, bins='auto', rwidth=0.8)
    plt.axvline(mean(data1), color='green')
    plt.axvline(1 / 12, color='red')
    plt.show()


