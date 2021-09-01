from playStats.descriptive_stats import *

if __name__ == '__main__':
    # # 频数
    # data = [2, 2, 2, 2, 1, 1, 1, 3, 3]
    # counter = Counter(data)
    # print(counter.most_common())
    # print(counter[2])
    #
    # # 频率
    # freq = frequency(data)
    # print(freq)
    #
    # # 众数
    # mod_elements, mode_cnt = mode(data)
    # print(mod_elements, mode_cnt)

    # 中位数
    data = [2, 2, 1, 4, 99, 4]
    med = median(data)
    print(med)

    mea = mean(data)
    print(mea)

    tiles = quartile(data)
    print(tiles)

    var = variance(data)
    print(var)
    print(std(data))
