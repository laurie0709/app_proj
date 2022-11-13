# coding:utf8
from flask import Flask

app = Flask(__name__)

app.debug = True

from app.admin import admin as admin_blueprint

app.register_blueprint(admin_blueprint, url_prefix="/admin")