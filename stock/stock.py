import tushare as ts
import matplotlib.pyplot as plt
import datetime

ticker = '000547'

# 获取历史行情数据
# finace=ts.get_hist_data(ticker)
# print("获取历史行情数据")
# print(finace)
#
# # 获取实时行情数据
# datato = ts.get_today_all(ticker)
# print("获取实时行情数据")
# print(datato)


# # 获取实时分笔数据
# data=ts.get_realtime_quotes(ticker)
# print("获取实时分笔数据")
# print(data)

# 获取当日历史分笔数据
data_today=ts.get_today_ticks(ticker)
print("获取当日历史分笔数据")
print(data_today)
data_today.to_csv('000547.csv')
data_today.to_excel('000547.xlsx')

