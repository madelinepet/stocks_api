from ..models.schemas import StocksSchema
from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
from pyramid.view import view_config
import requests



class StocksAPIViewset(APIViewSet):
    def create(self, request):
        """ creates a resource
        """
        return Response(json={'message': 'Created a new record'}, status=201)

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

        # try:
        #  WeatherLocation.remove(request=request, pk=id)

        # except(DataError, AttributeError):
            # return Response(json'Not Found', status=404)
        # return Response(status=204)



