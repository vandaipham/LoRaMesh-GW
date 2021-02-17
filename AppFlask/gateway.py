from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from AppFlask.auth import login_required
from AppFlask.db import get_db

from flask import jsonify
import json

bp = Blueprint('gateway', __name__)

@bp.route('/gateway')
@login_required
def gateway():
    return render_template('gateway/gateway.html')


@bp.route('/api/topology')
@login_required
def get_topology():
    f = open('G:\Dev_Space\LoRaMesh-GW\AppFlask\data.json')
    data = json.load(f)
    f.close()
    return jsonify(data)