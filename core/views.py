from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from .models import FAQ,TeamMember,services,publication,about,practicearea
from .forms import ContactForm

# Create your views here.

class indexView(View):
    def get(self, request):
        faqs = FAQ.objects.filter(category='Home'),
        practice = practicearea.objects.all()

        if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()  # Save the form data to the model
                return redirect('core:success')  # Redirect to the success page
        else:
            form = ContactForm()
        context = {
            'faqs': faqs,
            'form': form,
            'practice':practice
        }

        return render(request, 'index.html',context )


class AboutView(View):
    def get(self, request):
        faqs = FAQ.objects.filter(category='About')
        about_items = about.objects.all()
        context = {
            'faqs': faqs,
            'about_items': about_items,
        }
        return render(request, 'about.html',context)



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
    
class PublicationView(View):
    def get(self, request):
        publications = publication.objects.filter(is_services=False)
        context = {
            'publications': publications,
        }
        return render(request, 'publication.html',context)

    
class publicationdetailView(View):
    def get(self, request, slug):
        publication_obj = get_object_or_404(publication, slug=slug)
        return render(request, 'publication_detail.html', {
            'publication': publication_obj
        })

class ServiceView(View):
    def get(self, request):
        Service = services.objects.filter(is_services=True)
        return render(request, 'services.html',{'Service': Service})



def Contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the model
            return redirect('core:success')  # Redirect to the success page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'index.html')