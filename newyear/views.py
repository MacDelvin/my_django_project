from django.shortcuts import render
import datetime


# Create your views here.
def isitnewyear(request):
    now = datetime.datetime.now()
    return render(request, "newyr.html", {
        "newyear": now.month == 1 and now.day == 1
    })

# Create your views here.
