import json
from pprint import pprint

from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.serializers import Serializer,CharField,ChoiceField
from CollectingElement.WebScrapingClass import Webscrape
webscrape=Webscrape()
Choices=webscrape.get_headers()
class SetUrlSerializer(Serializer):
    def validate(self, data):
        urlparameter=data
        for key in Choices:
            if Choices[key]==urlparameter:
                return data
        raise serializers.ValidationError(f"Please Choose a Valid Name From This List:{list(Choices.values())}")
    def get_json_data(self):
        url_prameter=self.context['url_parameter']
        self.validate(data=url_prameter)
        web_scrape_object=Webscrape()
        data=web_scrape_object.json_data(name=url_prameter)
        return data





