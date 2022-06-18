from app import api
from flask import request
from flask_restful import Resource
from flask_cors import cross_origin
from app.services.tiktok_token_share_service import TiktokTokenShareService


class TiktokTokenShareController(Resource):

    def __init__(self):
        self.__tiktok_service = TiktokTokenShareService()

    @cross_origin()
    def post(self):
        data = request.get_json()
        address = data['address']
        tiktok_url = data['tiktok']
        return self.__tiktok_service.tiktok(address, tiktok_url)


api.add_resource(TiktokTokenShareController, '/api/drop/tiktok')
