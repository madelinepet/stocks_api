from ..models.schemas import StocksSchema
from ..models import Stock
from sqlalchemy.exc import IntegrityError, DataError
from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
from pyramid.view import view_config
import requests
import json


class StocksAPIViewset(APIViewSet):
    def create(self, request):
        """ creates a resource
        """
        try:
            kwargs = json.loads(request.body)
        except json.JSONDecodeError as e:
            return Response(json=e.message, status=400)
        try:
            stock = Stock.new(requests, **kwargs)
        except IntegrityError:
            return Response(json='Duplicate Key Error. Stock already exists', status=409)
        schema = StocksSchema()
        data = schema.dump(stock).data

        return Response(json=data, status=201)

    def list(self, request):
        """ Gets all
        """
        return Response(json={'message': 'Listing all the records'}, status=200)

    def retrieve(self, request, id=None):
        """ Gets one
        """
        return Response(json={'message': 'Listing one record'}, status=200)

    def destroy(self, request, id=None):
        """ Destroys a resource
        """
        if not id:
            return Response(status=204)

        try:
            Stock.remove(request=request, pk=id)

        except(DataError, AttributeError):
                return Response(json='Not Found', status=404)
        return Response(status=204)



