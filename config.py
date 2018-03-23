'''
@author:chenghuan
@time:2018/03/22
@博客的配置项文件
'''
import os
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ProcessPoolExecutor

PageNum = 4 #每页显示的文章个数

class WebConfig():
    SECRET_KEY = 'chenghuan'  #秘钥配置
    basedir = os.path.abspath(os.path.dirname(__file__))   #项目目录
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@127.0.0.1:3306/myblog'   #dialect+driver://username:password@host:port/database程序使用的数据库URL必须保存到SQLALCHEMY_DATABASE_URI变量
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True #每次请求结束都会自动提交事务
    SQLALCHEMY_TRACK_MODIFICATIONS = False#如果设置成True(默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。如果你不显示的调用它，在最新版的运行环境下，会显示警告。
    CSRF_ENABLED = True   #启用了跨站请求攻击保护
    UPLOAD_FOLDER = '/upload'
    DEBUG = True

def loadconfig():
    return WebConfig

class Config(object):
    JOBS = []
