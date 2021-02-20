from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from AppFlask.auth import login_required
from AppFlask.db import get_db

from flask import jsonify
import json
from flask import send_file

from os.path import join, dirname, realpath

bp = Blueprint('gateway', __name__)

@bp.route('/gateway')
@login_required
def gateway():
    return render_template('gateway/gateway_new.html')

@bp.route('/api/topology')
@login_required
def get_topology():
    data = getJson()
    return data

@bp.route('/api/get_image')
@login_required
def get_image():
    filename = './static/images/image.jpg'
    return send_file(filename, mimetype='image/jpg')

def getJson():
    dataPath = join(dirname(realpath(__file__)), 'static/data.json')
    f = open(dataPath)
    data = json.load(f)
    f.close()
    return data