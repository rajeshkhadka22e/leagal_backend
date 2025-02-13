from django.urls import path
from .views import indexView, ServiceView, AboutView,TeamView, TeamMemberDetailView,PublicationView,publicationdetailView

app_name = "core"

urlpatterns = [
    path('', indexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('team/', TeamView.as_view(), name='team'),
    path('team/<slug:slug>/', TeamMemberDetailView.as_view(), name='team_member_detail'),
    path('service/', ServiceView.as_view(), name='service'),
    path('publication/', PublicationView.as_view(), name='publication'),
    path('publication/<slug:slug>/', publicationdetailView.as_view(), name='publication_detail'),

]


