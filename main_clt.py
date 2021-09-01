# author:insthink
# contact: insthink@qq.com
# datetime:21/9/1 下午9:33
# software: PyCharm

import random

import matplotlib.pyplot as plt

from playStats.descriptive_stats import mean


def sample(num_of_samples, sample_sz, distribution_func):
    data = []
    for _ in range(num_of_samples):
        data.append(
            mean([distribution_func() for _ in range(sample_sz)])
        )
    return data


if __name__ == '__main__':
    data1 = sample(10000, 40, lambda: random.gauss(0, 1))
    plt.hist(data1, bins='auto', rwidth=0.8)
    plt.axvline(mean(data1), color='red')
    plt.show()
