from rest_framework.serializers import Serializer,CharField

class PriceSerializer(Serializer):
    Name=CharField()
