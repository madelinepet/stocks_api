from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='json', request_method='GET')
def home_view(request):
    """ configure a function that defines our home route,define type of
    renderer (analogous to content type), define a response
    """
    message = 'Hello World'
    return Response(body=message, status=200)


# @view_config(route_name='stocks', renderer='json', request_method='GET')
# def home_view(request):
#     """ configure a function that defines our home route,define type of
#     renderer (analogous to content type), define a response
#     """
#     message = 'Stocks'
#     return Response(body=message, status=200)
