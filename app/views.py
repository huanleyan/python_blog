"""
@author: lileilei
@file: views.py
@time: 2017/7/13 16:42
"""
from app import  app,db
from  flask import  make_response,redirect,request,render_template,session,url_for,flash,send_file,abort,make_response,send_from_directory,jsonify,Response
from werkzeug import secure_filename
from  app.models import *
from app.form import  *
import os,time,datetime
from flask.views import MethodView,View

class BlogView(MethodView):
    def get(self, id):
        return render_template('blog/index.html')
