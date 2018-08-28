from pyramid_restful.routers import ViewSetRouter
from .views import (StocksAPIViewset, CompanyAPIViewset, PortfolioAPIViewset, AuthAPIViewset)


def includeme(config):
    """ Binds the routes. The name 'includeme' has significance in pyramid as
    this function is scanned for and when found, does its job. All of the
    endpoints for view-controllers.
    """
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    router = ViewSetRouter(config)
    router.register('api/v1/portfolio', PortfolioAPIViewset, 'portfolio')
    router.register('api/v1/company', CompanyAPIViewset, 'company')
    router.register('api/v1/stock', StocksAPIViewset, 'stock')
    router.register('api/v1/auth/{auth}', AuthAPIViewset, 'auth')
