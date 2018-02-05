from django.core.mail import send_mail
from django.shortcuts import render

from .forms import Contact
from .models import Greeting


def index(request):
    return render(request, 'index.html')

def form(request):

    # Good abstraction but form is a django word and you shadow another variable
    form = Contact(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        try:
            send_mail('Funny feature :)',
            'Hey! (This automatic mail use Mailjet as a SMTP relay)',
            'alexis.aigue06@gmail.com',
            [email],
            fail_silently=False,)
        except:
            error = "Sending mail : an error occured"

        return render(request, 'resultForm.html', locals())

    return render(request, 'form.html', locals())

def more(request):
    return render(request, "more.html")

# You do not need that
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
