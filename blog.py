'''
@author:chenghuan
@time:2018/03/22
@入口文件
'''
from app import app
#from app.blog import blog
from config import Config
#app.register_blueprint(blog)

if __name__ == '__main__':
    app.config.from_object('config')  #加载额外的配置文件
    app.run(port=5003)
