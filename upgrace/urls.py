from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('get_followers/', include('insta_automation.urls')),
    path('generate_hashtags/', include('ihashtag.urls')),
    path('get_likes/', include('iliker.urls')),
    path('get_comments/', include('iliker.urls')),
    path('admin/', admin.site.urls),
]