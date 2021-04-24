from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def book(request):
    if request.method == "POST":
        # do stuff
        first_name = request.POST['firstname']
        e_mail = request.POST['email']
        budget = request.POST['Budget']
        Package = request.POST['Packages']

        #Send e_mail
        send_mail(
        first_name + ' is interested in one of your Safaris!',#Subject
        Package,#Message
        e_mail,#From Email
        ['mutwiri333@gmail.com'],#To Email
        )
        return render(request, 'TaiApp/contact.html', {'first_name':first_name})
    else:
        return render(request, 'TaiApp/contact.html')


class HomeView(TemplateView):
    template_name = 'TaiApp/index-4.html'

class PackagesView(TemplateView):
    template_name = 'TaiApp/Packages.html'

class NairobiView(TemplateView):
    template_name = 'TaiApp/Nairobi.html'

class BigfiveView(TemplateView):
    template_name = 'TaiApp/BigGame.html'

class BirdView(TemplateView):
    template_name = 'TaiApp/Birds.html'

class BeachView(TemplateView):
    template_name = 'TaiApp/ElephantSanctuary.html'

class nightView(TemplateView):
    template_name = 'TaiApp/MaasaiNight.html'

class nakuruView(TemplateView):
    template_name = 'TaiApp/LNakuru.html'

class maraView(TemplateView):
    template_name = 'TaiApp/MaraGame.html'

class maraSixView(TemplateView):
    template_name = 'TaiApp/sixDayMara.html'

class maraSevenView(TemplateView):
    template_name = 'TaiApp/sevenDayMara.html'

class nairobiParkView(TemplateView):
    template_name = 'TaiApp/NairobiPark.html'

# class bookView(TemplateView):
#     template_name = 'TaiApp/contact.html'
