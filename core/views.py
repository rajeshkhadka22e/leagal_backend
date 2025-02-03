from django.shortcuts import render
from django.views import View

# Create your views here.

class indexView(View):
    def get(self, request):
        return render(request, 'index.html')



class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')



class TeamView(View):
    def get(self, request):
        return render(request, 'team.html')




class ServiceView(View):
    def get(self, request):
        return render(request, 'services.html')
