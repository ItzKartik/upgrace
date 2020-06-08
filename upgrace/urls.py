from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ifollowers/', include('insta_automation.urls')),
    path('ihashtag/', include('ihashtag.urls')),
    path('iliker/', include('iliker.urls')),
    path('admin/', admin.site.urls),
]