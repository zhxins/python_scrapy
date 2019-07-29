import sys
import os
import matplotlib as mpl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def rowIndex(row):
    global plt
    if row.signal > 0:
        plt.annotate(u'买', xy=(row.date_o, row.signal), arrowprops=dict(facecolor='red', shrink=0.05))
    if row.signal < 0:
        plt.annotate(u'卖', xy=(row.date_o, row.signal))


if __name__ == "__main__":
    mpl.rcParams['font.sans-serif'] = [u'simHei']
    mpl.rcParams['axes.unicode_minus'] = False
    dateparse1 = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
    s_list = pd.read_csv("000547.csv", skiprows=0, encoding='utf-8', index_col='price', parse_dates=True, date_parser=dateparse1)
    s_list['date_o'] = s_list.index
    s_list['ma_sub'] = s_list['ma5'] - s_list['ma20']
    s_list['diff'] = np.sign(s_list['ma_sub'])
    s_list['signal'] = np.sign(s_list['diff'] - s_list['diff'].shift(1))
    s_list['signal'].plot(ylim=(-2, 2))
    (s_list['close']/40).plot(ylim=(-2, 2))
    s_list.apply(rowIndex, axis=1)
    plt.legend(loc='upper right')
    plt.grid(b=True)
    plt.show()

