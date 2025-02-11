from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import FAQ,TeamMember,publication
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
        team_members = TeamMember.objects.all() 
        team_members = TeamMember.objects.all().order_by('number') 
        context = {
            'team_members': team_members,
        }
        return render(request, 'team.html', context)

class TeamMemberDetailView(View):
    def get(self, request, slug):
        team_member = get_object_or_404(TeamMember, slug=slug) 
        context = {
            'team_member': team_member,
        }
        return render(request, 'team_member_detail.html', context)
class ServiceView(View):
    def get(self, request):
        return render(request, 'services.html')


class PublicationView(View):
    def get(self, request):
        publications = publication.objects.all()
        return render(request, 'publication.html',{'publications': publications})
