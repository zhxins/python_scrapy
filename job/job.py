# ！/usr/bin/env python
# -*-coding:utf-8-*-
"""
@Author  : xiaofeng
@Time    : 2018/12/18 16:31
@Desc : Less interests,More interest. (爬取智联招聘职位数据)
@Project : python_appliction
@FileName: zhilianzhaopin.py
@Software: PyCharm
@Blog    ：https://blog.csdn.net/zwx19921215
"""

import pymysql as db
import requests

# mysql配置信息
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'job',
    'charset': 'utf8'
}

# url
url = 'https://data.highpin.cn/api/JobSearch/Search'

"""
爬取智联招聘职位数据
@:param page 页码
@:param position 职位关键字
"""


def zhilian(page, position):
    # 封装头信息
    headers = {
        'Referer': 'https://www.highpin.cn/zhiwei/',
        'Origin': 'https://www.highpin.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Accept': 'application/json, text/javascript, * / *; q=0.01',
    }
    # 表单信息
    datas = {
        'Q': position,
        'pageIndex': page
    }
    resp = requests.post(url, data=datas, headers=headers)
    result = resp.json()
    return result


"""
控制台输出
"""


def print_data(result):
    body = result['body']['JobList']
    print(body)


"""
数据入库
"""


def insert(result):
    print("insert......")
    database = db.connect(**mysql_config)
    for item in result:
        print(item)
        sql = "INSERT INTO zhilian(JobID,JobTitle,ReferrerType,CompanyName,AnnualSalaryMin," \
              "AnnualSalaryMax,JobLactionStr,JobLactionID,JobTags\
        ,JobDegree,JobDegreeId,WorkExperience,WorkExperienceID,CompanyIndustry,CompanyIndustryID," \
              "CompanyType,CompanyTypeID,PublishDate,CompanyScale,SalaryWhite) \
              VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        # list convert to str
        JobLactionID = str(item['JobLactionID'])
        CompanyIndustryID = str(item['CompanyIndustryID'])

        if 'JobTags' in item:
            JobTags = str(item['JobTags'])
        else:
            JobTags = ''
        cursor = database.cursor()
        cursor.execute(sql, (
            item['JobID'], item['JobTitle'], item['ReferrerType'], item['CompanyName'], item['AnnualSalaryMin'],
            item['AnnualSalaryMax'],
            item['JobLactionStr'], JobLactionID, JobTags, item['JobDegree'], item['JobDegreeId'],
            item['WorkExperience'],
            item['WorkExperienceID'], item['CompanyIndustry'], CompanyIndustryID, item['CompanyType'],
            item['CompanyTypeID'], item['PublishDate'], item['CompanyScale'], item['SalaryWhite']))
        database.commit()
        cursor.close()
    database.close()


def main(position):
    result = zhilian(1, position)
    page_count = result['body']['PageCount']
    print("---------------共", page_count, "页-------------")
    page = 1
    while page <= page_count:
        print('----------------第', page, '页-----------------')
        result = zhilian(page, position)
        # print_data(result)
        body = result['body']['JobList']
        insert(body)
        page = page + 1


if __name__ == '__main__':
    main('java')