from flask import Blueprint, jsonify
from flask_restful import Api, Resource
import requests
import random

from model.cookie import *

cookie_api = Blueprint('cookie_api', __name__,
                      url_prefix='/api/cookies')

api = Api(cookie_api)

class CookiesAPI:
    # Create a new cookie (not implemented)
    class _Create(Resource):
        def post(self, cookie_type):
            pass
            
    # Get a list of all cookies
    class _Read(Resource):
        def get(self):
            return jsonify(getCookies())

    # Get information about a specific cookie type
    class _ReadType(Resource):
        def get(self, cookie_type):
            cookie = getCookie(cookie_type)
            if cookie:
                return jsonify(cookie)
            else:
                return {"message": "Cookie type not found."}, 404

    # Get a random cookie
    class _ReadRandom(Resource):
        def get(self):
            return jsonify(getRandomCookie())

    # Get the count of cookies
    class _ReadCount(Resource):
        def get(self):
            count = countCookies()
            countMsg = {'count': count}
            return jsonify(countMsg)

    # Buy a cookie
    class _UpdateBuy(Resource):
        def post(self, cookie_type):
            result = buyCookie(cookie_type)
            if 'message' in result:
                return result, 200
            else:
                return {"message": "Cookie type not found."}, 404

    api.add_resource(_Create, '/create/<string:cookie_type>')
    api.add_resource(_Read, '/')
    api.add_resource(_ReadType, '/<string:cookie_type>')
    api.add_resource(_ReadRandom, '/random')
    api.add_resource(_ReadCount, '/count')
    api.add_resource(_UpdateBuy, '/buy/<string:cookie_type>')

if __name__ == "__main__": 
    # Define the server URL
    server = 'https://flask.nighthawkcodingsociety.com'  # Update the URL as needed
    url = server + "/api/cookies"
    responses = []  # Responses list

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

    # Get a random cookie
    responses.append(
        requests.get(url + "/random")
    )

    # Cycle through responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")
