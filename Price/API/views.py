from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.mixins import RetrieveModelMixin,CreateModelMixin,ListModelMixin
from rest_framework.response import Response

from .serializers import SetUrlSerializer
class DetailView(ListAPIView,
                 ListModelMixin,
                 CreateModelMixin):
    permission_classes = []
    serializer_class = SetUrlSerializer
    def get_queryset(self):None
    def get(self, request, *args, **kwargs):
        name=self.request.GET.get('q')
        serialzer=SetUrlSerializer()
        serialzer.context['url_parameter']=name
        json_data=serialzer.get_json_data()
        return Response(json_data,status=status.HTTP_200_OK)

