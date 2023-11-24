# -*- coding: utf-8 -*-
# author: zy
from flask import make_response, jsonify

"""
编写自定义回复包装类
"""


def preprocessing(data, code, content_type="text/html"):
    """
    返回消息预处理

    :param data: 数据
    :param code: 返回编码
    :param content_type: 返回类型
    :return:
    """
    if content_type in ["text/html", "text/plain"]:
        data = str(data)
        # 处理页面中文乱码
        content_type += ";charset=UTF-8"
    elif content_type == "application/json":
        return make_response(jsonify(data), code)

    res = make_response(data, code)
    res.headers = {
        "content-type": content_type
    }
    return res


def message(data, res_type, code):
    """
    返回消息

    :param data: 数据
    :param res_type: 返回类型
    :param code: 返回代码
    :return:
    """
    if res_type == "html":
        return preprocessing(data, code=code, content_type="text/html")
    elif res_type == "text":
        return preprocessing(data, code=code, content_type="text/plain")
    elif res_type == "json":
        return preprocessing(data, code=code, content_type="application/json")
    else:
        return make_response(f"未知数据类型：{res_type}", 400)


def success(data, res_type="html", code=200):
    """
    成功返回消息

    :param data: 数据
    :param res_type: 返回类型
    :param code: 返回代码
    :return:
    """
    return message(data, res_type, code)


def error(data, res_type="text", code=400):
    """
    失败返回消息

    :param data: 数据
    :param res_type: 返回类型
    :param code: 返回代码
    :return:
    """
    return message(data, res_type, code)
