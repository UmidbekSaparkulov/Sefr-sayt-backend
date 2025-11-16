from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/core/', include('core.urls')),
    path('api/reading/', include('reading.urls')),
    path('api/writing/', include('writing.urls')),
    path('api/listening/', include('listening.urls')),
    path('api/speaking/', include('speaking.urls')),
]
