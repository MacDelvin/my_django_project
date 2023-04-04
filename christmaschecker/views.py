from django.shortcuts import render
import datetime


# Create your views here.
def isitchristmas(request):
    now = datetime.datetime.now()
    return render(request, "christ.html", {
        "christmas": now.month == 12 and now.day == 25
    })