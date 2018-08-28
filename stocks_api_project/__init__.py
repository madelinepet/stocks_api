from pyramid.config import Configurator
# from pyramid_restful.routers import CompanyAPIViewset


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('.models')
    config.include('pyramid_restful')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
