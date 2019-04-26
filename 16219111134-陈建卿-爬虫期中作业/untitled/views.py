from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
    city = '郑州市'
    url = 'http://api.map.baidu.com/telematics/v3/movie?qt=hot_movie&location='+city+'&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json'
    response = requests.get(url).json()

    if response.get('error') == 0:
        movies = response.get('result').get('movie')
        is_find=True
    else:
        movies =[]
        is_find =False,
    context = {
        'city': city,
        'movies': movies,
        'is_find': is_find
    }
    return render(request, 'index.html', context=context)


