import functools
import calendar
import requests
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for,jsonify
)

from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')
#查询每月标准工作日
@bp.route('/workingday',methods=('GET','POST'))
def workingday():
    code = request.json.get('code',None)
    Startdate = request.json.get('Startdate',None)
    enddate = request.json.get('enddate',None)
    state= request.json.get('state',None)
    url = 'http://findsoft.com.cn:8888/login.jsp'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
    getCookie = requests.get(url, headers=headers)
    Cookie=getCookie.cookies
    r = requests.post('http://findsoft.com.cn:8888/login.jsp?os_username=sunfucong&os_password=21yuanKU&os_cookie=true&os_destination=&user_role=&atl_token=&login=%E7%99%BB%E5%BD%95',headers=headers, cookies=Cookie,allow_redirects=False)
    wanmei = r.cookies
    url = 'http://findsoft.com.cn:8888/rest/api/2/search?jql=status+in+('+str(state)+')+AND+%E9%A6%96%E6%AC%A1%E8%A7%A3%E5%86%B3%E6%97%B6%E9%97%B4+%3E%3D+'+str(Startdate)+'+AND+%E9%A6%96%E6%AC%A1%E8%A7%A3%E5%86%B3%E6%97%B6%E9%97%B4+%3C%3D+'+str(enddate)+'+AND+%E5%BC%80%E5%8F%91%E8%80%85+in+('+str(code)+')&maxResults=500'
    g = requests.get(url,headers=headers, cookies=wanmei)
    getreurn = g.json()
    return jsonify(getreurn)
#注册接口
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.json.get('username',None)
        password = request.json.get('password',None)
        db = get_db()
        error = None

        if not username:
            error = '用户名不能为空！'
        elif not password:
            error = '密码不能为空！'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = '用户 {} 已经注册。'.format(username)
        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return '注册成功'
        flash(error)
    else:
        error = '不支持get请求'
    return error
#登录接口
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.json.get('username',None)
        password = request.json.get('password',None)
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()
        if not username.strip():
            tasks={
            'success':False,
            'data':'用户名不能为空！'
            }
            return jsonify(tasks)
        if user is None:
            tasks={
            'success':False,
            'data':'用户名不存在！'
            }
            resp = jsonify(tasks)
#            resp.status_code = 400
            return resp
        elif not check_password_hash(user['password'], password):
            tasks={
            'success':False,
            'data':'密码错误！'
            }
            return jsonify(tasks)
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            tasks={
            'success':True,
            'data':'登录成功'
            }
            return jsonify(tasks)


        flash(error)

    return error
    
    
#注销
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
   
#验证登录状态
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return '登录状态失效！'

        return view(**kwargs)

    return wrapped_view
