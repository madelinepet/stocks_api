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
            # pyramid_jwt docs
            return Response(
                json_body={
                    'token': request.create_jwt_token(
                        user.email,
                        roles=[role.name for role in user.roles],
                        userName=user.email,
                    )
                },
                status=201
            )

        if auth == 'login':
            authenticated = Account.check_credentials(request, data['email'], data['password'])
            if authenticated:
                return Response(
                    json_body={
                        'token': request.create_jwt_token(
                            authenticated.email,
                            roles=[role.name for role in authenticated.roles],
                            userName=authenticated.email,
                        )
                    },
                    status=201
                )
            return Response(json='Not Authorized', status=401)

        return Response(json='Route Not Found', status=404)
