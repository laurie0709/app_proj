# coding:utf8
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1 style='color:blue'>封面</h1>"


@app.route("/login/")
def login():
    return "<h1 style='color:blue'>登陆</h1>"


@app.route("/overview/")
def overview():
    return "<h1 style='color:blue'>养殖场总览</h1>"


@app.route("/production/monitor/")
def pro_monitor():
    return "<h1 style='color:blue'>生产监控</h1>"


@app.route("/production/feed/")
def pro_feed():
    return "<h1 style='color:blue'>饲料监控</h1>"


@app.route("/production/egg/")
def pro_egg():
    return "<h1 style='color:blue'>鸡蛋管理</h1>"


@app.route("/equipment/video_device/")
def equip_video():
    return "<h1 style='color:blue'>视频设备管理</h1>"


@app.route("/equipment/other_device/")
def equip_other():
    return "<h1 style='color:blue'>其他设备管理</h1>"


if __name__ == "__main__":
    app.run()
