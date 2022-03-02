from flask import *
from model import *
from flask import Blueprint, session, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash
from decorators import login_limit
import config

app = Flask(__name__)
#app.config.from_object(config)
#app.secret_key = "flaskblog"
# 注册蓝图
#from view import *

#app.register_blueprint(index)
#app.register_blueprint(blog)

#index = Blueprint("index",__name__) #实例化一个蓝图(Blueprint)对象
# 首页
@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
