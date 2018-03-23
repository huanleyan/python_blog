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
    def get(self, page):
        page=request.args.get('page',1,type=int)
        #results = (db.session.query(Blog.content.label('topic_content'), Category.content.label('cate_name'))).select_from(Topic, Reply).filter(Topic.id==Reply.topic_id).paginate(page, per_page)
        pagination = (db.session.query(Blog.blog_id,Blog.content,Blog.tags,Blog.title,Blog.desc,Blog.cate_id,Blog.comment_num,Blog.read_num,Blog.create_at,Category.cate_id, Category.cate_name)).select_from(Blog, Category).filter(Blog.cate_id==Category.cate_id).order_by(Blog.create_at.desc()).paginate(page, 4, False)
        blogs = pagination.items
        top3 = blogs[:3]
        tags = db.session.query(Tags).filter(Tags.status=='1').all()
        cates = db.session.query(Category).all()
        return render_template('blog/index.html', blogs=blogs,pagination=pagination, tags=tags, top3=top3, cates=cates)

class BlogDetailView(MethodView):
    def get(self, blog_id):
        #blog_id=request.args.get('blog_id',0,type=int)
        #blog = db.session.query(Blog).filter(Blog.blog_id==blog_id).first()
        blog = (db.session.query(Blog.blog_id,Blog.content,Blog.tags,Blog.title,Blog.desc,Blog.cate_id,Blog.comment_num,Blog.read_num,Blog.create_at,Category.cate_id, Category.cate_name)).select_from(Blog, Category).filter(Blog.cate_id==Category.cate_id, Blog.blog_id==blog_id).order_by(Blog.create_at.desc()).first()
        comments = db.session.query(Comment).filter(blog_id==blog_id).all()

        pagination = (db.session.query(Blog.blog_id,Blog.content,Blog.tags,Blog.title,Blog.desc,Blog.cate_id,Blog.comment_num,Blog.read_num,Blog.create_at,Category.cate_id, Category.cate_name)).select_from(Blog, Category).filter(Blog.cate_id==Category.cate_id).order_by(Blog.create_at.desc()).all()
        top3 = pagination[:3]
        tags = db.session.query(Tags).filter(Tags.status=='1').all()
        cates = db.session.query(Category).all()
        return render_template('blog/detail.html', blog=blog, comments=comments, top3=top3, tags=tags, cates=cates)
