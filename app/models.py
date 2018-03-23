# encoding: utf-8
"""
@author: chenghuan
@file: models.py
@time: 2018/3/13 16:43
"""
from  app import  db
import datetime
from werkzeug.security import check_password_hash,generate_password_hash
class Permisson:#这里的权限我是复制flask开发博客里面的，可以根据需求去修改
    FOLLOW = 0x01
    COMMENT = 0x02
    WRITE_ARTICLES = 0x04
    MODERATE_COMMENTS = 0x08
    ADMINISTRATOR = 0xff
