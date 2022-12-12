
from rest_framework.generics import ListAPIView
from rest_framework.mixins import RetrieveModelMixin
from .serializers import PriceSerializer
class DetailView(ListAPIView,RetrieveModelMixin):
    permission_classes = []
    serializer_class = PriceSerializer
    def get_queryset(self):None

    def get(self, request, *args, **kwargs):
        return self.list(request,*args,**kwargs)


