from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotAcceptable , ValidationError
from classifier.functions import text_binary_classification
# Create your views here.
class ClassifyView(APIView):
    def post(self, request):
        string_list = request.data.get('string_list', None)
        if not string_list:
            raise NotAcceptable('You should pass a list of strings!')
        if type(string_list) != type(list()):
            raise ValidationError('You should pass your strings in a list')
        for item in string_list:
            if type(item) != str:
                raise ValidationError('Please pass only strings in your list')
        print(string_list)
        print(type(string_list))
        tag_list = text_binary_classification(string_list)
        print(tag_list)
        dict = {}
        for s in range(len(string_list)):
            dict[string_list[s]] = tag_list[s]

        return Response(dict)