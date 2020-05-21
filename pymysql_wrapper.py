#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys;
import pymysql.cursors
import db_config
import time
#import __builtin__

class ConnectSession(object):
    """docstring for Connection"""
    def __init__(self, ConnectionName):
        self.start_time = 0
        self.end_time = 0
        self.ConnectionName = ConnectionName
        super(ConnectSession, self).__init__()
        self.conn=self.Connect(ConnectionName)

    def Connect(self, ConnectionName):
        self.start_time = time.time()
        #print("Start_time : %s " % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.start_time)))
        if ConnectionName in db_config.db_config:
            dbmsg=db_config.db_config[ConnectionName]

            con_info = ""
            for key, value in dbmsg.items():
                con_info += "\t\t%-9s : %s\n" %(key, value)
            #print('DBConnect    %s, Connect_Info:\n%s' % (self.ConnectionName, con_info[:-2]))
            #conn = pymysql.connect(host='123.58.188.132',user='shshixingang',password="shshixingang",port=3306,charset=dbmsg['charset'])
            #conn = pymysql.connect(host='192.168.104.93',user='dj_online',password="dj_online",port=3306,charset=dbmsg['charset'])

            try:
                conn=pymysql.connect(host=dbmsg['host'],user=dbmsg['usr'],password=dbmsg['password'],port=dbmsg['port'],charset=dbmsg['charset'])
            except Exception:
                return
            sql='select NOW();'
            cur = conn.cursor();
            cur.execute(sql)
            NowTime=cur.fetchall()
            cur.close()
            return conn

    def Disconnect(self):
        if self.conn:
            self.conn.close()
            print('DBDisConnect %s' % self.ConnectionName)
            self.end_time = time.time()
            print("End_time : %s " % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.start_time)))
            total_time = int(self.end_time - self.start_time)
            print("Total_times %s min %s s " % (total_time/60, total_time%60))


class ConnectionMgn(object):
    def __init__(self):
      self.connection_dict={}

    def AddConnection(self, ConnectionName):
        if ConnectionName in self.connection_dict:
            print('always have connection %s'%ConnectionName)
        else:
            conn = ConnectSession(ConnectionName)
            self.connection_dict[ConnectionName] = conn

    def InitConnection(self, ConnectionName):
        return self.AddConnection()

    def RemoveConnection(self, ConnectionName):
        if ConnectionName in self.connection_dict:
            conn = self.connection_dict.pop(ConnectionName)
            conn.Disconnect()
        else:
            return None

    def GetConnection(self, ConnectionName):
        return self.connection_dict.get(ConnectionName,None)

    def GetConnection_New(self, ConnectionName):
        self.AddConnection(ConnectionName)
        conn = self.connection_dict.get(ConnectionName,None)
        if None != conn:
            return conn.conn

def InitDB():
    db_config.Global_dir['db'] = ConnectionMgn()

InitDB()




