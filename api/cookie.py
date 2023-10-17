from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, request, Resource # used for REST API building
import requests  # used for testing
import random
from __init__ import login_manager, app, db
from model.cookie import Cookie

cookie_api = Blueprint('cookie', __name__, url_prefix='/api/cookie')
# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1


api = Api(cookie_api)
class cookies:
    class _getCookies(Resource):
        def get(self):
            cookies = db.session.query(Cookie).all()
            return jsonify([cookie.alldetails() for cookie in cookies])
        
    class _getcookiedetails(Resource):
        def get(self):
            cookie = db.session.query(Cookie).filter(Cookie.id == int(request.args.get("id"))).first()
            return jsonify(cookie.alldetails())
    
    api.add_resource(_getCookies, "/cookies")
    api.add_resource(_getcookiedetails, "/cookiedetails")