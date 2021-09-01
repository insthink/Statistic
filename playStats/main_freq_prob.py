# author:insthink
# contact: insthink@qq.com
# datetime:21/8/29 下午10:56
# software: PyCharm

import random

import matplotlib.pyplot as plt


def toss():
    return random.randint(0, 1)


if __name__ == '__main__':
    indices = []
    freq = []
    for toss_num in range(10, 1000001, 1000):
        heads = 0
        for _ in range(toss_num):
            if toss() == 0:
                heads += 1
        freq.append(heads / toss_num)
        indices.append(toss_num)
    plt.plot(indices, freq)
    plt.show()