# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import OrderedDict
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .task import change_status


def create_response(response_data):
    """
    method used to create response data in given format
    """
    response = OrderedDict()
    response["header"] = {"status": "1"}
    response["body"] = response_data["data"]
    return response


def create_error_response(response_data):
    """
    method used to create response data in given format
    """
    return OrderedDict({"header": {"status": "0"},"errors": response_data})


class CreateItemAPIView(APIView):

    def post(self, request):
        serializer = CreateItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            change_status.delay(serializer.data)
            return Response(create_response({"data": serializer.data}))
        else:
            return Response(
                create_error_response(serializer.errors),status=403)