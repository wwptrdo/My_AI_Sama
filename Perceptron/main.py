# -*- coding: utf-8 -*-

#统计学习方法：P29 例2.1
# author：wwptrdudu
# date: 2018.10.08

import numpy as np
import matplotlib.pyplot as plt
import time

def test():
    plt.style.use('seaborn-whitegrid')
    fig = plt.figure()
    ax = plt.axes()
    ax.set(xlim=(0, 6), ylim=(0, 6),
           xlabel='X(1)', ylabel='Y(2)')
    ax.cla()
    X = np.array([[3, 3],
                  [4, 3],
                  [1, 1]])
    Y = np.array([1, 1, -1])

    ax.plot([x for x in X[:, 0]],[x for x in X[:, 1]],
            'o', color='black')

    w, b = [0, 0], 0

    wang = np.linspace(-10, 10, 1000)

    while True:
        I = [0, 1, 2]
        R = np.array([False, False, False])
        for i in I:
            print("\n点", i+1, ": ", X[i])
            print("判定：", Y[i]*(w*X[i]+b))
            # 未正确分类，更新w, b
            if np.all((Y[i]*(w*X[i]+b)) <= 0):
                w, b = w+Y[i]*X[i], b+Y[i]

                if (w[1] != 0):
                    ax.cla()
                    ax.axis('equal')
                    ax.plot([x for x in X[:, 0]],[x for x in X[:, 1]],
                            'o', color='black')
                    wei = -1 * (b+w[0]*wang)/w[1]
                    ax.plot(wang, wei)
                    fig.show()
                    time.sleep(1)
                    print("更新了一次图片！")

                print("未正确分类，更新w, b = ", w, b)
            else:
                R[i] = True
                print("正确分类！")
            time.sleep(1)

        if np.all(R):
            break

    return


if __name__ == "__main__":
    test()
