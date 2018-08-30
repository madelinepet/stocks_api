from pyramid.config import Configurator
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Allow, ALL_PERMISSIONS
# from pyramid_restful.routers import CompanyAPIViewset


# class that contains tuples with policies
class RootACL(object):
    __acl__ = [
        (Allow, 'admin', ALL_PERMISSIONS),
        (Allow, 'view', ['read'])
    ]

    # need this __init__ here to turn in req
    def __init__(self, request):
        pass


def add_role_principals(userid, request):
        # gets roles on the jwt (claims to permissions) and makes available
        # for the rest of the workflow to use
        return request.jwt_claims.get('roles', [])


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application, and looks for
    includeme functions.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jwt')
    config.include('pyramid_restful')

    config.set_root_factory(RootACL)
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.set_jwt_authentication_policy(
        'superseekretseekrit',  # os.environ.get('SECRET', None)
        # bearer auth is for json web tokens
        auth_type='Bearer',
        callback=add_role_principals,
    )

    config.include('.models')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
