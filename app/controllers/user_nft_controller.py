from app import api
from flask_restful import Resource
from flask_cors import cross_origin
from app.services.user_nft_service import UserNftService


class UserNftController(Resource):

    def __init__(self):
        self.__user_nft_service = UserNftService()

    @cross_origin()
    def get(self, **type):
        address = None
        if type.get('address') is not None:
            address = str(type.get('address'))

        return self.__user_nft_service.user_nfts(address)


api.add_resource(UserNftController, '/api/nft/<string:address>')
