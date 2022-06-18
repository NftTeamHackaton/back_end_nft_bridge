from app import api
from flask import request
from flask_restful import Resource
from flask_cors import cross_origin
from app.services.twitter_token_share_service import TwitterTokenShareService


class TwitterTokenShareController(Resource):

    def __init__(self):
        self.__twitter_service = TwitterTokenShareService()

    @cross_origin()
    def post(self):
        data = request.get_json()
        address = data['address']
        twitter_username = data['twitter_username']
        return self.__twitter_service.twitter_repost(address, twitter_username)


api.add_resource(TwitterTokenShareController, '/api/drop/twitter')
