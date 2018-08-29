# TODO: finish this- refactor Resonse with 'created' to use a JSON web token

from pyramid_restful.viewsets import APIViewSet
from sqlalchemy.exc import IntegrityError
from pyramid.response import Response
from ..models import Account
import json


class AuthAPIViewset(APIViewSet):
    def create(self, request, auth=None):
        """ Use a post method to both create or register and to log in.
        First, get the data from the body of the req
        """
        data = json.loads(request.body)

        if auth == 'register':
            try:
                user = Account.new(
                    request,
                    data['email'],
                    data['password'])
            except(IntegrityError, KeyError):
                return Response(json='Bad Request', status=400)

            return Response(json='Created', status=201)

        if auth == 'login':
            pass

        return Response(json='Route Not Found', status=404)
