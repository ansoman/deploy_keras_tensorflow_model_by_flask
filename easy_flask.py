# -*- coding: utf-8 -*-
"""
# @Time : 2019/9/4 8:57
# @Author : fab
# @FileName: easy_flask.py
"""
# 加载Flask
import flask
app = flask.Flask(__name__)
# 将一个预测函数定义为一个端点
@app.route("/predict", methods=["GET","POST"])
def predict():
    data = {"success": False}
    # 获取请求参数
    params = flask.request.json
    print(params)
    if (params == None):
        params = flask.request.args
    # 若获得参数，则回显msg 参数
    if (params != None):
        data["response"] = params.get("msg")
        print(data)
        data["success"] = True
    # 返回一个 json 格式的响应
    return flask.jsonify(data)
# 开启Flask应用程序，运行远程连接
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)