from flask import Blueprint, jsonify
from flask_restful import Api, Resource, reqparse
from __init__ import db
from model.cookie import Cookie

cookie_api = Blueprint('cookie', __name__, url_prefix='/api/cookie')

api = Api(cookie_api)

class CookieListResource(Resource):
    def get(self):
        cookies = db.session.query(Cookie).all()
        return jsonify([cookie.alldetails() for cookie in cookies])

class CookieDetailsResource(Resource):
    def get(self, cookie_id):
        cookie = db.session.query(Cookie).filter(Cookie.id == cookie_id).first()
        if cookie:
            return jsonify(cookie.alldetails())
        return jsonify({"message": "Cookie not found"}), 404

api.add_resource(CookieListResource, "/cookies")
api.add_resource(CookieDetailsResource, "/cookies/<int:cookie_id>")
