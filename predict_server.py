# -*- coding: utf-8 -*-
"""
# @Time : 2019/9/3 20:11
# @Author : fab
# @FileName: predict_server.py
"""
# 加载库
import flask
import pandas as pd
import tensorflow as tf
import keras
from keras.models import load_model
import numpy as np

# 实例化 flask
app = flask.Flask(__name__)

# 我们需要重新定义我们的度量函数，
# 从而在加载模型时使用它


def auc(y_true, y_pred):
    auc1 = tf.metrics.auc(y_true, y_pred)[1]
    keras.backend.get_session().run(tf.local_variables_initializer())
    return auc1


# 加载模型，传入自定义度量函数
global graph
graph = tf.get_default_graph()
model = load_model('games.h5', custom_objects={'auc': auc})

# 将预测函数定义为一个端点
@app.route("/predict", methods=["GET", "POST"])
def predict():
    data = {"success": False}
    params = flask.request.json
    if params is None:
        params = flask.request.args

    # 若发现参数，则返回预测值
    if params is not None:
        x = np.array(params["data"]).reshape(1,-1)
        with graph.as_default():
            data["prediction"] = str(model.predict(x)[0][0])
            data["success"] = True

    # 返回Jason格式的响应
    return flask.jsonify(data)


# 启动Flask应用程序，允许远程连接
app.run(host='0.0.0.0',port=5050)
