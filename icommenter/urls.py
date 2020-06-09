from django.contrib import admin
from django.urls import path
from icommenter import views
from django.views.generic import TemplateView

app_name = 'icommenter'

urlpatterns = [
    path('', TemplateView.as_view(template_name='icommenter/index.html'), name='index'),
    path('commentit/', views.icommenter.as_view(), name='icommenter_url'),
]
