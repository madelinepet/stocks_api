from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
import requests


class CompanyAPIViewset(APIViewSet):

    def retrieve(self, request, id=None):
        url = 'https://api.iextrading.com/1.0/stock/{}/company'.format(id)
        response = requests.get(url)
        return Response(json=response.json(), status=200)
        # http://localhost:6543/api/v1/company/{id}/
        # use the id to lookup that resource in the DB
        # formulate a response and send it back to the client

    # An example
    # def list_all_companies(self, request):
    #     # http://localhost:6543/api/v1/company/
