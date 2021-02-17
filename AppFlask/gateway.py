from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from AppFlask.auth import login_required
from AppFlask.db import get_db

from flask import jsonify
import json
from flask import send_file


bp = Blueprint('gateway', __name__)

@bp.route('/gateway')
@login_required
def gateway():
    return render_template('gateway/gateway.html')


@bp.route('/api/topology')
@login_required
def get_topology():
    f = open('D:\Dev_Workspace\LoRaMesh-GW\AppFlask\data.json')
    data = json.load(f)
    f.close()
    return jsonify(data)

@bp.route('/api/get_image')
@login_required
def get_image():
    filename = 'D:\Dev_Workspace\LoRaMesh-GW\AppFlask\static\images\image.jpg'
    return send_file(filename, mimetype='image/jpg')