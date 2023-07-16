import logging

from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import Pupil, Interactive, News


def home(request):
    return render(request, 'petshelter/home.html')


def news(request):
    try:
        newses = News.objects.order_by('-created')
    except IntegrityError:
        logging.critical("Bd crush @home@", IntegrityError)
    return render(request, 'petshelter/news.html', {'newses': newses})


def interactive(request):
    try:
        interactives = Interactive.objects.order_by('-created')
    except IntegrityError:
        logging.critical("Bd crush @home@", IntegrityError)
    return render(request, 'petshelter/interactive.html', {'interactives': interactives})


def helpus(request):
    try:
        pupils = Pupil.objects.order_by('-created')
    except IntegrityError:
        logging.critical("Bd crush @home@", IntegrityError)
    return render(request, 'petshelter/helpus.html', {'pupils': pupils})


def about(request):
    return render(request, 'petshelter/about.html')


def telegram(request):
    return redirect('https://t.me/Naryana_bot')

