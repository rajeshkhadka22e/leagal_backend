from django.urls import path
from .views import indexView, ServiceView, TeamView, AboutView

app_name = "core"

urlpatterns = [
    path('', indexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('team/', TeamView.as_view(), name='team'),
    path('service/', ServiceView.as_view(), name='service'),
]
