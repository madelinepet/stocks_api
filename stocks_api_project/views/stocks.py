from ..models.schemas import StocksSchema
from ..models import Stock
from sqlalchemy.exc import IntegrityError, DataError
from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
import requests
import json


class StocksAPIViewset(APIViewSet):
    def create(self, request):
        """ creates a resource in the database. The most robust of the methods.
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
        """ Gets all records from the db using marshmallow schema to serialize
        and send back the data in a response
        """
        records = Stock.all(request)
        schema = StocksSchema()
        data = [schema.dump(record).data for record in records]
        return Response(json=data, status=200)

    def retrieve(self, request, id=None):
        """ Gets one record from the db using marshmallow like with list
        """
        record = Stock.one(request, id)
        if not record:
            return Response(json='Not found', status=404)
        schema = StocksSchema()
        data = schema.dump(record).data
        return Response(json=data, status=200)

    def destroy(self, request, id=None):
        """ Destroys a resource from the db
        """
        if not id:
            return Response(status=204)

        try:
            Stock.remove(request=request, pk=id)

        except(DataError, AttributeError):
                return Response(json='Not Found', status=404)
        return Response(status=204)
