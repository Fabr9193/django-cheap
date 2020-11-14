from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests

from api.local_settings import TEQUILA_API_KEY

# Create your views here.

def home(request):

    url = 'https://tequila-api.kiwi.com/v2/search'
    headers = {'apiKey' : TEQUILA_API_KEY}
    params = {'fly_from':'PAR', 'dateFrom':'18/11/2020','dateTo':'12/12/2020','price_to':20, 'curr':'USD'}
    
    # POST :  
    if request.method == 'GET':
        params = {'fly_from':request.GET.get('fly_from'), 'dateFrom':request.GET.get('dateFrom'),'dateTo':request.GET.get('dateTo'),'price_to':request.GET.get('price_to'), 'curr':'USD'}
    #--
    response = requests.get(url,params=params,headers=headers)
    return JsonResponse(response.json(), safe=False)
