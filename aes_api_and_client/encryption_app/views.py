from django.shortcuts import render
from django.http import HttpResponse
from encryption_app import models
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
import json

"""
{
    "key":"my name is varun",
    "mode":"e",
    "values":[
        "str1","str2"
    ]

}
"""

str1 = '{"key":"","mode":"d","values":["i5K2FOf1Zry1FPMIPwtJsLsRa7KW8ldA6scyX9Ol1y4="]}'

@api_view(['GET', 'POST'])
def index(request):
    #return Response(json.dumps(request.data))
    if request.method == 'POST':
            executor = models.AESExecutor()
            result = executor.execute(json.dumps(request.data))
            return Response(result)
    else:
        return Response({"UsageError": 'Send a post request of the form: {"key":"key","mode":"e/d","values":["str1","str2",...]}' #+ form
  })


    