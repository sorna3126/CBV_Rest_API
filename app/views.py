from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from app.serializers import *

# Create your views here.


class ProductCRUD(APIView):
    def get(self,request):
        PDO=Product.objects.all()
        PJD=ProductModelSerializer(PDO,many=True)
        return Response(PJD.data)

    def post(self,request):
        JDO=request.data
        PMSD=ProductModelSerializer(data=JDO)
        if PMSD.is_valid():
            PMSD.save()
            return Response('{Data is inserted Successfully}')
        else:
            return Response('{Data is not inserted }')
