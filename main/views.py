from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Salwa Hafiza Aqila",
        "npm": "2506624392",
        "study_program": "S1 Information Systems",
        "bio": (
            "Hi! I’m Salwa, an Information Systems student at Universitas Indonesia who loves trying new things and taking on new challenges. I’m passionate about growing through every experience, meeting new people, and continuously improving myself along the way."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Salwa",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)