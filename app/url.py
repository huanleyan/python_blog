# -*- coding: utf-8 -*-
# @Date    : 2017-08-09 20:05:32
# @Author  : lileilei
from app.views import *
from app import app
app.add_url_rule('/blog/<int:id>',view_func=BlogView.as_view('blog_get'))
