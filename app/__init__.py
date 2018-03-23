'''
@author:chenghuan
@time:2018/03/22
@博客的配置项文件
'''
#ImportError: No module named 'MySQLdb'   https://www.cnblogs.com/TaleG/p/6735099.html
import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import loadconfig
#app是Flask的实例，它接收包或者模块的名字作为参数，但一般都是传递__name__。
app = Flask(__name__)
cnf = loadconfig()
app.config.from_object(cnf)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

from app import views, models, url
