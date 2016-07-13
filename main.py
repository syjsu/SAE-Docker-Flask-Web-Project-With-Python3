import os
from flask import Flask

import sae.kvdb

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello():
	return "我的第一个SAE容器的Flask案例"

@app.route('/user/<name>')
def user(name):
	return "你好,%s" % name
	
@app.route('/post/<int:id>')
def show_post(id):
    return '您的id号码是%d' % id

@app.route()
def kv():
	kv = sae.kvdb.Client()
	k = 'foo'
	kv.set(k, 2)
	kv.add(k, 3)
	print(kv.get(k))
	
@app.errorhandler(404)
def not_found(error):
    return '对不起，您访问的网页找不到 %d' % 404
	
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5050)