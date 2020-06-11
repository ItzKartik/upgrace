from django.contrib import admin
from django.urls import path
from insta_automation import views
from django.views.generic import TemplateView

app_name = 'ihashtag'

urlpatterns = [
    path('', TemplateView.as_view(template_name='ihashtag/index.html'), name='index'),
]
