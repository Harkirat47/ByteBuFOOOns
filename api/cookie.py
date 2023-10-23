from flask import Blueprint, jsonify
from flask_restful import Api, Resource, reqparse
from __init__ import db
from model.cookies import Cookie  # Import the Cookie model

# Create a Blueprint for the Cookie API
Cookie_api = Blueprint('Cookie_api', __name__, url_prefix='/api/Cookie')

# Create the API instance
api = Api(Cookie_api)

class CookieAPI(Resource):
    def get(self):
        # Retrieve all cookies from the database
        cookies = Cookie.query.all()

        # Prepare the data in JSON format
        json_ready = [cookie.to_dict() for cookie in cookies]

        # Return the JSON response
        return jsonify(json_ready)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("cookie_name", required=True, type=str)
        parser.add_argument("image", required=True, type=str)
        parser.add_argument("stock", required=True, type=int)
        parser.add_argument("price", required=True, type=float)  # Change type to float for price
        args = parser.parse_args()

        try:
            cookie = Cookie(
                cookie_name=args["cookie_name"],
                image=args["image"],
                stock=args["stock"],
                price=args["price"]
            )
            db.session.add(cookie)
            db.session.commit()
            return cookie.to_dict(), 201
        except Exception as exception:
            db.session.rollback()
            return {"message": f"Error: {exception}"}, 500

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        parser.add_argument("cookie_name", type=str)
        parser.add_argument("image", type=str)
        parser.add_argument("stock", type=int)
        parser.add_argument("price", type=float)  # Change type to float for price
        args = parser.parse_args()

        try:
            cookie = db.session.query(Cookie).get(args["id"])
            if cookie:
                if args["cookie_name"] is not None:
                    cookie.cookie_name = args["cookie_name"]
                if args["image"] is not None:
                    cookie.image = args["image"]
                if args["stock"] is not None:
                    cookie.stock = args["stock"]
                if args["price"] is not None:
                    cookie.price = args["price"]  # Fix the attribute name here
                db.session.commit()
                return cookie.to_dict(), 200
            else:
                return {"message": "Cookie not found"}, 404
        except Exception as exception:
            db.session.rollback()
            return {"message": f"Error: {exception}"}, 500


    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        args = parser.parse_args()

        try:
            cookie = db.session.query(Cookie).get(args["id"])
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
api.add_resource(CookieAPI, "/")

class CookieListAPI(Resource):
    def get(self):
        # Retrieve all cookies from the database
        cookies = Cookie.query.all()

        # Prepare the data in JSON format
        json_ready = [cookie.to_dict() for cookie in cookies]

        # Return the JSON response
        return jsonify(json_ready)
    
# Add the CookieListAPI resource to the /api/Cookie endpoint
api.add_resource(CookieListAPI, "/")
