# from pyramid_restful.viewsets import APIViewSet
# from pyramid.response import Response


#  @view_config(route_name='lookup', renderer='json', request_method='GET')
#     def lookup(request):
#     """ Makes the 3rd party api call
#     """
#     # insert base URL here
#     url = 'postgres://localhost:5432'
#     response = request.get(url)
#     return Response(json=response.json(), status=200)

# class CompanyAPIViewset(APIViewSet):


#     def retrieve(self, request, id=None):
#         # http://localhost:6543/api/v1/company/{id}/
#         # use the id to lookup that resource in the DB
#         # formulate a response and send it back to the client
#         return Response(
#             json={'message': 'Provided a single resource'},
#             status=200
#             )

#     # An example
#     # def list_all_companies(self, request):
#     #     # http://localhost:6543/api/v1/company/

