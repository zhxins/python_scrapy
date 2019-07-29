import matplotlib.pyplot as plt
from sqlalchemy import false
import numpy as np


def echart1():
    labels='frogs','hogs','dogs','logs'
    sizes=15,20,25,10
    colors='yellowgreen','gold','lightskyblue','lightcoral'
    explode=0,0.1,0,0
    plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=False,startangle=0)
    plt.title('Top 10 GDP Countries', bbox={'facecolor': '0.8', 'pad': 5})
    plt.axis('equal')
    plt.show()


def echart2():
    import numpy as np
    import matplotlib.pyplot as plt

    # evenly sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)

    # red dashes, blue squares and green triangles
    plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
    plt.show()

def echart3():
    import numpy as np
    import matplotlib.pyplot as plt

    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)

    # 数据的直方图
    n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    # 添加标题
    plt.title('Histogram of IQ')
    # 添加文字
    plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.axis([40, 160, 0, 0.03])
    plt.grid(True)
    plt.show()


def echart4():
    import numpy as np
    import matplotlib.pyplot as plt

    ax = plt.subplot(111)

    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2 * np.pi * t)
    line, = plt.plot(t, s, lw=2)

    plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 )

    plt.annotate('local min', xy=(3.5, -1.0), xytext=(4.5, -1.5),
                 arrowprops=dict(facecolor='red', shrink=0.05),
                 )
    plt.ylim(-2, 2)
    plt.show()


def echart5():
    import numpy as np
    import matplotlib
    from matplotlib import pyplot as plt
    matplotlib.rcParams['font.sans-serif'] = 'Microsoft Yahei'  # 改字体为微软雅黑，以便显示中文
    fig, ax = plt.subplots()

    animal = {"锯齿动物": 38, "蝙蝠类": 21.8, "食虫类": 8.2, "灵长类": 8, "其他": 6.9, "有袋类": 6.5, "食肉类": 5.6, "偶蹄类": 5}  # 创建数据
    data = np.array([i for i in animal.values()]).astype(float)  # 饼图显示数据，将其转换成float格式
    label = np.array([j for j in animal.keys()])  # 设置标签
    ax.pie(data, labels=label, autopct='%.1f%%', startangle=90, counterclock=False,
           wedgeprops=dict(width=0.61, edgecolor='w'))  # autopct为显示百分比，startangle为起始角度，counterclock逆时针选否
    ax.set_title("哺乳动物类群")  # 设置标题
    ax.axis("equal")  # 设置x轴和y轴等长，否则饼图将不是一个正圆

    plt.show()


def echart6():
    x = np.linspace(0, 2 * np.pi, 10)
    y1, y2 = np.sin(x), np.cos(x)

    plt.plot(x, y1, 'ro-')
    plt.plot(x, y2, 'g*:', ms=10)
    plt.show()


if __name__ == "__main__":
    echart6();
    # echart4();