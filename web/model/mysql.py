import time
import pymysql
from decimal import Decimal
import json

def get_conn():
    """
    :return: 连接，游标
    """
    # 创建连接
    conn = pymysql.connect(host="47.94.95.145",
                           user="root",
                           password="123456",
                           db="Jingdong",
                           port=3306,
                           charset="utf8")
    # 创建游标
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    return conn, cursor


def close_conn(conn, cursor):
    cursor.close()
    conn.close()


def query(sql, *args):
    """
    封装通用查询
    :param sql:
    :param args:
    :return: 返回查询到的结果，((),(),)的形式
    """
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res

def get_comment_data():
    """
    :return: 返回大屏div id=c1 的数据
    """
    # 因为会更新多次数据，取时间戳最新的那组数据
    sql = "SELECT phone_id,user_content,user_score,id FROM Jingdong.`jd comments`"
    res = query(sql)
    res_list = []
    for i in res:
        # for j in i:
        res_list.append(list(i))

    # res_list = [str(i) for i in res[0]]
    # res_tuple=tuple(res_list)
    # print(res_list)
    return res_list

def get_info_data():
    """
    :return: 返回大屏div id=c1 的数据
    """
    # 因为会更新多次数据，取时间戳最新的那组数据
    sql = "SELECT phone_name,phone_price,feedback FROM Jingdong.`jd info`"
    res = query(sql)
    res_list = []
    for i in res:
        # for j in i:
        res_list.append(list(i))

    # res_list = [str(i) for i in res[0]]
    # res_tuple=tuple(res_list)
    # print(res_list)
    return res_list