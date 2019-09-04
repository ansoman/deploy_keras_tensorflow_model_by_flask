# deploy_keras_tensorflow_model_by_flask
使用flask部署深度学习模型
1.train.py训练模型并保存；
2.使用predict_server.py部署服务，需注意的是
global model
model = load_model(model_path)
以及在预测时：
with graph.as_default():
在调用模型预测前需加这句话，不然会引起线程安全问题；
3.部署服务后即可在postman测试啦；
