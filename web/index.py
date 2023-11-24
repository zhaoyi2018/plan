# -*- coding: utf-8 -*-
# author: zy
# 导入Flask类库
from flask import Flask
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

# 创建应用实例
app = Flask(__name__,
            template_folder=os.path.join(dir_path, "resources", "templates"),
            static_folder=os.path.join(dir_path, "resources", "static"))

# JSON中的中文乱码处理
app.config['JSON_AS_ASCII'] = False

# 导入路由
from route import *

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=51212)
