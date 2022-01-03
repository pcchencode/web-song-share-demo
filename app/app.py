#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
from flask import Flask
# from flask_pymongo import PyMongo # pip install flask_pymongo
import pymysql as db# pip install pymysql
# from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import jsonify
from flask import render_template
from view_form import SongForm, SearchForm
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY']='your key' #這是因為flask_wtf預設需要設置密碼，也是為了避免一開始所說的CSRF攻擊。

@app.route('/')
def index():
    return "SUCCESS"

@app.route('/home-page')
def home_page():
    return render_template('home2.html', home_active='active')

@app.route('/test2-sql')
def test_sql():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'test'
    }
    conn = mysql.connector.connect(**config)
    cur = conn.cursor()
    sql = "SELECT * FROM `test`.`guitar_song`"
    cur.execute(sql)
    u = cur.fetchall() # 返回 tuple 
    conn.close()
    return f"hello {u}"

@app.route('/song-share', methods=['GET', 'POST'])
def song_share():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'test'
    }
    conn = mysql.connector.connect(**config)
    cur = conn.cursor()
    form = SongForm()
    #  flask_wtf類中提供判斷是否表單提交過來的method，不需要自行利用request.method來做判斷
    if form.validate_on_submit():
        s_name = request.values.get('song_name')
        author = request.values.get('author')
        desc = request.values.get('desc')
        url = request.values.get('url')
        sql = f"""
        INSERT INTO guitar_song(`name`, `desc`, `url`) VALUES ('{s_name}', '{desc}', '{url}')
        """
        # print(sql)
        try:
            cur.execute(sql)
            conn.commit()
            return render_template('submit_success.html', s_name=s_name, share_now_active='active')
        except Exception as e:
            conn.rollback()
            print(e)
            return render_template('submit_failed.html', err=e, share_now_active='active')
        # return f'Success Submit {s_name} {desc} {url}'
    #  如果不是提交過來的表單，就是GET，這時候就回傳user.html網頁
    return render_template('guitar_song.html', form=form, share_now_active='active')


@app.route('/query-song', methods=['GET', 'POST'])
def query_song():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'test'
    }
    conn = mysql.connector.connect(**config)
    # conn = db.connect(host=host_name, user=user_name, password=password, port=port, db=db_name)
    # conn = db.connect(host='127.0.0.1', user='root', password='', port=3306, db='test')
    cur = conn.cursor()
    form = SearchForm()
    if form.validate_on_submit():
        q_name = request.values.get('query_name')
        sql = f"""
        SELECT `id`, `name`, `author`, `desc`, `url` FROM `test`.`guitar_song`
        WHERE `name`= '{q_name}'
        """
        print(sql)
        cur.execute(sql)
        res = cur.fetchall() # 返回 tuple
        conn.close()
        if len(res)>0:
            # return f"your query result {res}"
            return render_template('query_result.html', result=res, search_active='active', query_name=q_name)
        else:
            return render_template('query_failed.html', search_active='active')
    else:
        return render_template('query_song.html', form=form, search_active='active')



if __name__ == '__main__':
    app.config['SECRET_KEY']='your key' #這是因為flask_wtf預設需要設置密碼，也是為了避免一開始所說的CSRF攻擊。
    app.run(host="0.0.0.0", port=5000) # to any port##
