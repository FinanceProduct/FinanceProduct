from django.shortcuts import render
from django.conf import settings

# Create your views here.
def searchbank(request):
    context = {
        'KAKAO_JAVASCRIPT_KEY': settings.KAKAO_JAVASCRIPT_KEY,
    }
    return render(request, 'bank/searchbank.html', context)