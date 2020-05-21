#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import os.path
import sys
import pymysql_wrapper
from   pymysql import converters
import db_config

import datas.enwords as enwords

##############################################################

def get_worlds_info_by_db(search_info):
    conn_local = db_config.Global_dir['db'].GetConnection_New(db_config.connection_name)

    try:
        db_curs = conn_local.cursor()
    except Exception:
        return False


    sql_auth = 'SELECT word, translation FROM abc_103976.enwords where word like "%%%s%%";' % search_info
    #print (sql_auth)
    db_curs.execute(sql_auth)
    #result = db_curs.fetchone()
    en_to_cn = False
    for each in db_curs:
        if not en_to_cn: en_to_cn = True
        gen_info = "{:20s},{:20s}".format(each[0], each[1])
        print(gen_info)

    if not en_to_cn:
        sql_auth = 'SELECT word, translation FROM abc_103976.enwords where translation like "%%%s%%";' % search_info
        #print (sql_auth)
        db_curs.execute(sql_auth)
        for each in db_curs:
            gen_info = "{:20s},{:20s}".format(each[0], each[1])
            print(gen_info)

    db_curs.close()
    return True


def get_worlds_info_by_local(search_world):
    all_datas = enwords.enwords

    en_to_cn = False
    print("\n\tSearch by Local Datas\n")
    print("    ALL result contain words : %s\n" % search_world)
    for en, cn in all_datas.items():
        if en.find(search_world) != -1:
            if not en_to_cn: en_to_cn= True
            gen_info = "{:20s},{:20s}".format(en, cn)
            print(gen_info)
    if en_to_cn:
        return
    else:
        new_dict = {v : k for k, v in all_datas.items()}
        for cn, en in new_dict.items():
            if cn.find(search_world) != -1:
                gen_info = "{:20s},{:20s}".format(en, cn)
                print(gen_info)
    return

def Main(search_world):
    if not get_worlds_info_by_db(search_world):
        get_worlds_info_by_local(search_world)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(" \nmust have a word to be search！！")
        sys.exit()
    Main(sys.argv[1])
