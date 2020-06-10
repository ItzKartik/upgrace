from django.contrib import admin
from django.urls import path
from insta_automation import views
from django.views.generic import TemplateView

app_name = 'insta_automation'

urlpatterns = [
    path('', TemplateView.as_view(template_name='insta_automation/index.html'), name='index'),
    path('followers/', views.Followers.as_view(), name='follow_him'),
    # path('flw_count/', views.flw_count, name='follow_count'),
]
