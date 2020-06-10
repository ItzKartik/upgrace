from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('get_followers/', include('insta_automation.urls')),
    path('generate_hashtags/', include('ihashtag.urls')),
    path('get_likes/', include('iliker.urls')),
    path('get_comments/', include('icommenter.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
