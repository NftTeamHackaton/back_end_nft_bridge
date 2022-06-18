from app import api
from flask import request
from flask_restful import Resource
from flask_cors import cross_origin
from app.services.create_nft_service import CreateNftService


class CreateNftController(Resource):

    def __init__(self):
        self.__create_nft = CreateNftService()

    @cross_origin()
    def post(self):
        # name, picture, description, chain_id,  address, user_address
        data = request.get_json()
        name = data['name']
        picture = data['picture']
        description = data['description']
        chain_id = data['chain_id']
        address = data['address']
        user_address = data['user_address']

        return self.__create_nft.create_nft(name, picture, description, chain_id, address, user_address)

    @cross_origin()
    def put(self):
        data = request.get_json()
        address = data['address']
        chain_id = data['chain_id']
        return self.__create_nft.edit_nft(address, chain_id)


api.add_resource(CreateNftController, '/api/create/nft')
