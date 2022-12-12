from rest_framework.serializers import Serializer,CharField

class PriceSerializer(Serializer):
    Name=CharField()
    WeekRange=CharField()
    Circulating_supply=CharField()
    Days_Range=CharField()
    Maket_Cap=CharField()
    Max_Supply=CharField()
    Open=CharField()
    Previous=CharField()
    RegularMarketChange=CharField()
    RegularMarketChangePercent=CharField()
    StartDate=CharField()
    Volume=CharField()
    Volume_24H=CharField()
    Volum_24H_All_Currencies=CharField()


class SetUrlSerializer:
    Url=CharField()

    def create(self):
        pass


