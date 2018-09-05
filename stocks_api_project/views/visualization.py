from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class VisualizationAPIViewset(APIViewSet):
    def list(self, request):
        """ Gets the chart
        """
        return Response(json={'message': 'Listing the chart'}, status=200)
