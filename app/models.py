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

class Blog(db.Model):#博客基础表
    __tablename__='blog'
    blog_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)  #blogid
    #project_user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    title = db.Column(db.String(255))#博客名称
    desc = db.Column(db.String(),default='')#描述
    content = db.Column(db.String(),default='')#内容
    cate_id = db.Column(db.Integer())#分类ID
    tags = db.Column(db.String(),default='')#标签
    comment_num = db.Column(db.Integer())#评论数量
    read_num = db.Column(db.Integer())#阅读数量
    create_at = db.Column(db.String())#阅读数量

class Category(db.Model):  #分类表
    __tablename__='category'
    cate_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)  #分类ID
    #project_user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    cate_name = db.Column(db.String(255))#分类名称

class Tags(db.Model):  #标签表
    __tablename__='tags'
    tag_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)  #标签ID
    tag_name = db.Column(db.String(255))#标签名称
    status = db.Column(db.Integer())#是否显示
