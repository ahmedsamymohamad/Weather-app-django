from django.shortcuts import render
import requests
import os

def Home(request):
    """ Api From Weatherbit.io """

    key = os.environ['WEATHERBIT_API_KEY']
    url = 'https://api.weatherbit.io/v2.0/current?lat={}&lon={}&key={}'


    if request.method == "POST":
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']

        try:
            result = requests.get(url.format(latitude,longitude,key)).json()

        except:
            print('try again')

        context ={
            "latitude": latitude,
            "longitude": longitude,
            'temp':result['data'][0]['temp']

        }
    else:
        context = {}
    return render(request,'index.html',context)