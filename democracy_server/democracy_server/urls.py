from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('public_api.urls')),
    path('', include('frontend_server.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# (marwan): this last line enables routing all /media/.. requests to
#           directly serve files from the MEDIA_ROOT path defined in
#           the settings file