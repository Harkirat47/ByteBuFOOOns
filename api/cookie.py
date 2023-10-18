from flask import Blueprint, jsonify
from flask_restful import Api, Resource, reqparse
from __init__ import db
from model.cookie import Cookie  # Import the Cookie model

# Create a Blueprint for the Cookie API
Cookie_api = Blueprint('Cookie_api', __name__, url_prefix='/api/Cookie')

# Create the API instance
api = Api(Cookie_api)

class CookieAPI(Resource):
    def get(self, id):
        # Retrieve a single cookie by its ID from the database
        cookie = Cookie.query.get(id)

        if cookie:
            return cookie.to_dict(), 200
        else:
            return {"message": "Cookie not found"}, 404

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("Cookie_name", type=str)
        parser.add_argument("image", type=str)
        parser.add_argument("stock", type=str)
        parser.add_argument("price", type=str)
        args = parser.parse_args()

        try:
            cookie = db.session.query(Cookie).get(id)
            if cookie:
                if args["Cookie_name"] is not None:
                    cookie.Cookie_name = args["Cookie_name"]
                if args["image"] is not None:
                    cookie.image = args["image"]
                if args["stock"] is not None:
                    cookie.stock = args["stock"]
                if args["price"] is not None:
                    cookie.price = args["price"]
                db.session.commit()
                return cookie.to_dict(), 200
            else:
                return {"message": "Cookie not found"}, 404
        except Exception as exception:
            db.session.rollback()
            return {"message": f"Error: {exception}"}, 500

    def delete(self, id):
        try:
            cookie = db.session.query(Cookie).get(id)
            if cookie:
                db.session.delete(cookie)
                db.session.commit()
                return cookie.to_dict()
            else:
                return {"message": "Cookie not found"}, 404
        except Exception as exception:
            db.session.rollback()
            return {"message": f"Error: {exception}"}, 500

# Add the CookieAPI resource to the /api/Cookie/<int:id> endpoint
api.add_resource(CookieAPI, "/<int:id>")

class CookieListAPI(Resource):
    def get(self):
        # Retrieve all cookies from the database
        cookies = Cookie.query.all()

        # Prepare the data in JSON format
        json_ready = [cookie.to_dict() for cookie in cookies]

        # Return the JSON response
        return jsonify(json_ready)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Cookie_name", required=True, type=str)
        parser.add_argument("image", required=True, type=str)
        parser.add_argument("stock", required=True, type=str)  # Adjust the type to int
        parser.add_argument("price", required=True, type=str)  # Adjust the type to float
        args = parser.parse_args()
        cookie = Cookie(args["Cookie_name"], args["image"], args["stock"], args["price"])

        try:
            db.session.add(cookie)
            db.session.commit()
            return cookie.to_dict(), 201
        except Exception as exception:
            db.session.rollback()
            return {"message": f"Error: {exception}"}, 500

# Add the CookieListAPI resource to the /api/Cookie endpoint
api.add_resource(CookieListAPI, "/")
