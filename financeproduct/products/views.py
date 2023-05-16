from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

from .models import DepositOptions, DepositProducts
from .serializers import DepositOptionsSerializer, DepositProductsSerializer
# Create your views here.

BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

# @api_view(['GET'])
# def api_test(request):
#     URL = BASE_URL + 'depositProductsSearch.json'
#     params = {
#         'auth': settings.API_KEY,
#         'topFinGrpNo': '020000',
#         'pageNo': 1
#     }
#     response = requests.get(URL, params=params).json()
#     return JsonResponse({ 'response': response })

@api_view(['GET'])
def save_deposit_products(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': settings.API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1,
    }
    response = requests.get(URL, params=params).json()
    serializer = DepositProductsSerializer(data=response['result']['baseList'], many=True)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return JsonResponse({ 'status': 'success' })
    else:
        return JsonResponse({ 'status': 'fail', 'message': serializer.errors })
    
@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        deposits = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(deposits, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse({ 'status': 'success'})
        else:
            return JsonResponse({ 'status': 'fail', 'message': serializer.errors })

@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    deposit = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositProductsSerializer(deposit)
    return JsonResponse(serializer.data)

@api_view(['GET'])
def top_rate(request):
    deposit = DepositOptions.objects.order_by('-intr_rate').first()
    serializer = DepositOptionsSerializer(deposit)
    return JsonResponse(serializer.data)
