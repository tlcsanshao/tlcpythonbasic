import pandas as pd
import mysql.connector
import datetime
from datetime import datetime as dt


def calculate_year_month_week(date):
    # 将日期字符串转换为 datetime 对象
    date_obj = date

    # 计算年份和月份
    year = date_obj.year
    month = date_obj.month

    # 计算第几周
    week = (date_obj.isocalendar())[1]

    return year, month, week


# 自定义类来表示对象
class MyObject:
    def __init__(self, project_id, date, user_id, activity_id, issue_id, hours):
        self.project_id = project_id
        self.date = date
        self.user_id = user_id
        self.activity_id = activity_id
        self.issue_id = issue_id
        self.hours = hours


def getData():
    # 读取 Excel 文件
    df = pd.read_excel('gongshi.xlsx')

    list = []
    # 逐行读取数据
    for index, row in df.iterrows():
        obj = MyObject(row['project_id'], row['日期'].to_pydatetime(), row['user_id'], row['activity_id'], row['问题'], row['小时'])
        list.append(obj)
        # print(obj.project_id,obj.date,obj.user_id,obj.activity_id,obj.issue_id,obj.hours)

    return list


def connect(list):
    try:
        # 连接到 MySQL 数据库
        conn = mysql.connector.connect(
            host="192.168.18.234",
            user="root",
            password="h5u4d10f",
            database="bitnami_redmine"
        )

        # 创建游标对象
        cursor = conn.cursor()

        # 创建表
        # cursor.execute("CREATE TABLE IF NOT EXISTS userst (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")

        for obj in list:
            # 插入数据
            year, month, week = calculate_year_month_week(obj.date)
            sql = "INSERT INTO time_entries (project_id,author_id,user_id,issue_id,hours,activity_id,spent_on,created_on,updated_on,tyear,tmonth,tweek) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s,%s,%s,%s)"
            val = (obj.project_id, obj.user_id, obj.user_id, obj.issue_id, obj.hours, obj.activity_id, obj.date, obj.date, obj.date, year, month, week)
            cursor.execute(sql, val)

        # 提交更改
        conn.commit()

        # 查询数据
        # cursor.execute("SELECT * FROM userst")
        # rows = cursor.fetchall()

        # 打印结果
        # for row in rows:
        #     print(row)

    except mysql.connector.Error as err:
        print("MySQL 错误：", err)

    finally:
        # 关闭游标对象和连接
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()


if __name__ == '__main__':
    print("开始执行")
    time1 = dt.now()
    list = getData()
    print("需要插入的数据量为", len(list))
    connect(list)
    print("执行完毕")
    time2 = dt.now()
    timediff = (time2 - time1).total_seconds()
    print("时间差为", timediff, "秒")
