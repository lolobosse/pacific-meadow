import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

from .models import Greeting
from .forms import Contact


def index(request):
    return render(request, 'myIndex.html')

def form(request):

    form = Contact(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        try:
            send_mail('I finally achieved this optionnal feature :)',
            'Hey! (This automatic mail use Mailjet as a SMTP relay)',
            'alexis.aigue06@gmail.com',
            [email],
            fail_silently=False,)
        except:
            error = "Sending mail : an error occured"

        return render(request, 'resultForm.html', locals())

    return render(request, 'myForm.html', locals())

def more(request):
    return render(request, "more.html")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
