# encoding: utf-8
"""
@author: lileilei
@file: form.py
@time: 2017/7/13 16:42
"""
from flask_wtf import  Form
from wtforms import  StringField,SubmitField,DateTimeField,validators,IntegerField,FileField,PasswordField,SelectField
from wtforms.validators import Email
#from app.models import Work

class LoginFrom(Form):
    username=StringField(u'用户名',[validators.Length(min=4, max=16,message=u'用户名长度在4-16位'),validators.DataRequired()],render_kw={'placeholder':u'请输入用户名'})
    password=PasswordField(u'密码',[validators.length(min=8,max=16,message=u'密码长度8-16位'),validators.DataRequired()],render_kw={'placeholder':u'请输入密码'})
