from pyramid_restful.routers import ViewSetRouter
from .views import StocksAPIViewset, CompanyAPIViewset


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    router = ViewSetRouter(config)
    config.add_route('stocks', '/api/v1/stocks')
    router.register('api/v1/stocks', StocksAPIViewset, 'stocks')
    router.register('api/v1/company', CompanyAPIViewset, 'company')
    # confid.add_route('lookup', '/api/v1/lookup/{zip_code}')
