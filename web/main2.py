# -*- coding: utf-8 -*-
# author: zy

# 导入Flask类库
from flask import Flask, make_response, jsonify, redirect, abort

"""
    cookie和session是用于服务器识别客户端的工具, cookie数据主要存放在浏览器端, session数据主要存放在服务端
    session和token都用于识别客户端, 从开发角度, session更安全(不可跨域), token更通用(可跨域).所以三者, 只要实现一者就可
    
    from flask import request
    request.url: 完整请求路径, 是不是可以修改路径
    request.method: 请求方法类型，是不是可以根据方法类型调用不同的操作
    request.remote_addr: 远程地址, 是不是可以作为防火墙
    request.args: 获取get请求参数
    request.json: 获取post请求的参数
    request.header: header信息, 是否可以添加授权信息
    request.cookie.get: 缓存获取, 可用于记录客户端通用信息
    
    @app.route('/') 请求钩子装饰器, 一个函数可绑定多个@app.route
    before_first_request: 第一次请求之前, 是否可以作为防火墙验证, cookie和session的建立
    before_request: 每次请求之前, 授权信息验证, cookie和session的获取
    app.after_request: 没有异常, 每次请求之后。是否可以作为日志记录
    app.teardown_request: 有异常也会运行, 每次请求结束后。可作为异常日志记录
    app.route('/', methods=["GET", "POST"]) 默认GET请求, 可允许不同请求
    
    @app.route('/<param>') 带参数的装饰器
    默认为str类型, 可指定（int, float, path）-> /<int:param>。 可用于快速获取url上的信息
    
    from flask import make_response, jsonify
    make_response响应构造函数: 一般视图函数默认返回headers的content-type类型都为text/html, 我们可以通过返回对象, 设置其他的返回类型和
    状码。我们是不是可以通过包装make_response, 自定义各种项目需要的返回结构
    jsonify: 将字典转为可发送给前端的json格式, 自动修改content-type为application/json
    
    from flask import redirect 可用于处理授权验证失败后, 跳转登录页面
    redirect('https://www.baidu.com') 跳转外网
    redirect('/路由名/') 跳转其他路径
    redirect(url_for('函数名', 函数参数)) 跳转指定函数
    
    from flask import render_template, g
    render_template('index.html') 通过g.params传参, 是否可用于设置所有页面的标题等通用数据
    render_template('index.html', params=value) 通过函数传参, 处理各用户数据
    
    在index.html文件中, 设置动态参数
    {{ param }}: 临时参数
    {{ g.param }}: 全局参数
    {{ param|capitalize }}: 对参数处理展示
        capitalize 首字母大写
        upper 全部大写
        lower 全部小写
        title 每个单词首字母大写
        trim 去掉两边的空白
        striptags 去掉所有的HTML标签
        safe 即删除标签，又保留标签功能
    
    在index.html文件中, 语法
    {{ params }}: 表示变量
    {# name #}: 表示备注
    {% if name %}{% else %}{% endif %}: 表示if
    {% for name in names %}{{ name }}{% endfor %}: 表示for
    
    宏的使用 就是一种类似vue的组件
"""

# 创建应用实例
app = Flask(__name__)


# 视图函数
@app.route('/')
def index():
    # 调到 index 路由
    # return redirect('/index')
    res = make_response("登录失败!", 404)
    res.headers = {
        'content-type': 'text/plain'
    }
    abort(res)


# 视图函数
@app.route('/index')
def say_hello():
    return '<h1>Hello World<h1>'


# 视图函数
@app.route('/test/<path:info>')
def test(info):
    return f'<h1>{info}<h1>', 404


# 视图函数
@app.route('/response')
def response():
    data = {'data': [1, 2, 3]}
    # headers = {
    #     'content-type': 'application/json'
    # }
    res = make_response(jsonify(data), 200)
    # res.headers = headers
    return res


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=51212)
