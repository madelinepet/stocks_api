from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class StocksAPIView(APIViewSet):
    def list(self, request):
        """ Gets all
        """
        return Response(json={'message': 'Listing all the records'}, status=200)

    def retrieve(self, request):
        """ Gets one
        """
        return Response(json={'message': 'Listing one record'}, status=200)

    def create(self, request):
        """ creates a resource
        """
        return Response(json={'message': 'Created a new record'}, status=201)

    def destroy(self, request):
        """ Destroys a resource
        """
        return Response(json={'message': 'Deleted the record'}, status=204)


