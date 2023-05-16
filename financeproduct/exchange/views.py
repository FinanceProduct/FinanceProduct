from django.shortcuts import render
from django.conf import settings
import requests
from datetime import datetime
# Create your views here.

def exchange(request):
    return render(request, 'exchange/exchange.html')

def calculate_exchange_rate(request):
    amount = float(request.GET.get('amount'))
    from_currency = request.GET.get('from_currency')
    to_currency = request.GET.get('to_currency')
    
    api_key = settings.EXCHANGE_API_KEY  # 한국수출입은행 API 키
    
    current_date = datetime.now()
    current_date = current_date.strftime("%Y%m%d")
    api_url = f"https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&searchdate={current_date}&data=AP01"

    response = requests.get(api_url)
    data = response.json()
    print(data)
    exchange_rate = None
    for item in data:
        if item['cur_unit'] == from_currency:
            rate1 = item['deal_bas_r']
            rate1 = rate1.replace(',', '')
            rate1 = float(rate1)
        if item['cur_unit'] == to_currency:
            rate2 = item['deal_bas_r']
            rate2 = rate2.replace(',', '')
            rate2 = float(rate2)
    exchange_rate = rate1 / rate2
    
    if exchange_rate is not None:
        result = amount * float(exchange_rate)
        result = round(result, 2)
        result_message = f"{amount} {from_currency} = {result} {to_currency}"
    else:
        result_message = "환율 정보를 가져올 수 없습니다."
        
    return render(request, 'exchange/exchange.html', {'result_message': result_message})