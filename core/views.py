from django.shortcuts import render
from django.views import View
from .models import FAQ
# Create your views here.

class indexView(View):
    def get(self, request):
        faqs = FAQ.objects.all()
        return render(request, 'index.html', {'faqs': faqs})



class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')



class TeamView(View):
    def get(self, request):
        return render(request, 'team.html')




class ServiceView(View):
    def get(self, request):
        return render(request, 'services.html')
