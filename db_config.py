#!/usr/bin/python
# -*- coding: utf-8 -*-
import binascii
import struct


Global_dir = {}

db_config = {
    "db_info" : {
      'host'     : 'XXX.XXX.XXX.XX',
      'port'     : 3306,
      'usr'      : 'geekpanshi',
      'password' : 'geekpanshi',
      'charset'  : 'gb2312',
      'db_name'  : 'abc_103976',
    }
}

connection_name= "db_info"
