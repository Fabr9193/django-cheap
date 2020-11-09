from django.shortcuts import render
from django.http import HttpResponse
import requests

from api.local_settings import *

# Create your views here.

def home(request):

    url = 'https://tequila-api.kiwi.com/v2/search'
    headers = {'apiKey' : TEQUILA_API_KEY}
    params = {'fly_from':'PAR', 'dateFrom':'18/11/2020','dateTo':'12/12/2020','price_to':20, 'curr':'USD'}
    response = requests.get(url,params=params,headers=headers)
    print(response)
    return HttpResponse("the response text is %s" %  response.text)
