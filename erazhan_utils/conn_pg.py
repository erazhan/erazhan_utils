# -*- coding = utf-8 -*-
# @time: 2022/4/18 5:08 下午
# @Author: erazhan
# @File: conn_pg.py

# ----------------------------------------------------------------------------------------------------------------------
import pymysql
import psycopg2

class MysqlConnection(object):
    def __init__(self,
                 host,
                 port,
                 user,
                 passwd,
                 database,
                 charset = 'utf8'):

        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database
        self.charset = charset

    def get_conn(self, conn_type="psycopg"):

        if conn_type == "psycopg":
            conn = psycopg2.connect(
                database=self.database,
                user=self.user,
                password=self.passwd,
                port=self.port,
                host=self.host
            )

        if conn_type == "pymysql":
            conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                passwd=self.passwd,
                db=self.database,
                charset=self.charset,
            )
        return conn

    def query(self, sql, conn_type='psycopg'):

        conn = self.get_conn(conn_type=conn_type)
        cur = conn.cursor()

        cur.execute(sql)
        ans = cur.fetchall()

        cur.close()
        conn.close()

        return ans

    def insert_data_many(self, sql, data, conn_type="pymysql"):

        conn = self.get_conn(conn_type=conn_type)
        cur = conn.cursor()
        cur.executemany(sql, data)
        conn.commit()
        cur.close()
        conn.close()

        return

    def truncate(self, table):

        sql = "truncate table %s" % table
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()

        return

    def create_table(self, create_sql):
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute(create_sql)
        conn.commit()
        cur.close()
        conn.close()

    def delete(self, delete_sql):

        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute(delete_sql)
        conn.commit()
        cur.close()
        conn.close()