import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for,jsonify
)

from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

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
