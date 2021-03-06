from django.shortcuts import render
import requests
from .forms import *
from .models import *
from django.contrib import messages
import datetime
# Create your views here.


def index(request):
    context = {}
    return render(request, "user_sys/index.html", context)


def scientific_labs(request):
    context = {}
    return render(request, "user_sys/scientific_labs.html", context)


def laboratory_booking(request):
    if request.method == "POST":
        dateTime = datetime.datetime.today()
        mobile_num = request.POST.get("mobileNumber")
        email = request.POST.get("email")
        address = request.POST.get("addressField")
        city = request.POST.get("cityField")
        state = request.POST.get("stateField")
        lastCropSown = request.POST.get("lastCropSown")
        soilType = request.POST.get("soilType")
        cropType = request.POST.get("cropType")
        lab_booking_save = LaboratoryBooking(
            dateTime=dateTime, mobileNumber=mobile_num, email=email, addressField=address, cityField=city, stateField=state, lastCropSown=lastCropSown, soilType=soilType, cropType=cropType)
        lab_booking_save.save()
        messages.success(request, 'Your form has been submitted successfully!')

    return render(request, "user_sys/laboratoryBookingForm.html")


def market(request):
    context = {}
    return render(request, "user_sys/market.html", context)


def weather_forecast(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=2ebe62ad7ad9ab7bf60a9e5bf054180e'

    if request.method == 'POST':
        form = WeatherForm(request.POST)
        form.save()

    form = WeatherForm()

    city = Weather.objects.last()

    r = requests.get(url.format(city)).json()
    print(r)
    city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'humidity': r['main']['humidity'],
        'feels_like': r['main']['feels_like'],
        'temperature_min': r['main']['temp_min'],
        'temperature_max': r['main']['temp_max'],
        'pressure': r['main']['pressure'],
        'wind_speed': r['wind']['speed'],
        'visibility': r['visibility']
    }
    # print(city_weather)
    context = {
        'city_weather': city_weather,
    }
    return render(request, "user_sys/weather_forecast.html", context)


def farm_ed(request):
    context = {}
    return render(request, "user_sys/farm_ed.html", context)


def video_gallery(request):
    context = {}
    return render(request, "user_sys/videobar.html", context)


def login(request):
    context = {}
    return render(request, "user_sys/login.html", context)


def register(request):
    context = {}
    return render(request, "user_sys/register.html", context)


def irrigation(request):
    context = {}
    return render(request, "user_sys/irrigation.html", context)


def newtech(request):
    context = {}
    return render(request, "user_sys/newtech.html", context)


def queryform(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        query = request.POST.get('query')
        des = request.POST.get('des')
        queryform = QueryForm(phone=phone, email=email, query=query, des=des)
        queryform.save()
        messages.success(request, 'Your form has been submitted successfully!')

    return render(request, "user_sys/queryform.html")


def videobar(request):
    context = {}
    return render(request, "user_sys/videobar.html", context)


def product(request):
    context = {}
    return render(request, "user_sys/product.html", context)


def team(request):
    context = {}
    return render(request, "user_sys/team.html", context)


def contact(request):
    context = {}
    return render(request, "user_sys/contact.html", context)

def faq(request):
    context = {}
    return render(request, "user_sys/faq.html", context)
