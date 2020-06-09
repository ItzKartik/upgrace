from django.contrib import admin
from django.urls import path
from iliker import views
from django.views.generic import TemplateView

app_name = 'iliker'

urlpatterns = [
    path('', TemplateView.as_view(template_name='iliker/index.html'), name='index'),
    path('likeit/', views.iliker.as_view(), name='iliker_url'),
]
