# -*- coding: utf-8 -*-
# author: zy
from flask import render_template, request

from index import app
from reponse import success, error
import backend.data_provision as service


# 主页面
@app.route('/')
def index():
    return success(render_template('index.html', menu_list=service.get_menu_list()))


# 数据获取
@app.route('/query_all_list')
def query_all_list():
    return success(service.query_all_list(), res_type="json")


# 创建任务
@app.route('/create_new_plan', methods=["POST"])
def create_new_plan():
    params = request.json
    plan_name = params["plan_name"]
    start_time = params["start_time"]
    list_nums = params["list_nums"]
    return success(service.create_new_plan(plan_name, start_time, list_nums), res_type="json")


# 推迟任务
@app.route('/delay_plan', methods=["POST"])
def delay_plan():
    params = request.json
    return success(service.delay_plan(), res_type="json")


# 加快任务
@app.route('/speed_up_plan')
def speed_up_plan():
    return success(service.speed_up_plan(), res_type="json")


# 添加任务章节
@app.route('/add_new_chapter')
def add_new_chapter():
    return success(service.add_new_chapter(), res_type="json")


# 删除任务章节
@app.route('/delete_chapter')
def delete_chapter():
    return success(service.delete_chapter(), res_type="json")


# 查看任务详情
@app.route('/detail_plan')
def detail_plan():
    return success(service.detail_plan(), res_type="json")