from app import api
from flask_restful import Resource
from flask_cors import cross_origin
from app.services.visitors_first_site_service import VisitorsFirstSiteService
from flask import request


class VisitorsFirstSiteController(Resource):

    def __init__(self):
        self.__visitors_first = VisitorsFirstSiteService()

    @cross_origin()
    def post(self):
        data = request.get_json()
        address = data['address']
        ip_address = request.remote_addr
        return self.__visitors_first.first_visit(address, ip_address)


api.add_resource(VisitorsFirstSiteController, '/api/statistic/visit')
