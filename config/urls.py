from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_prometheus.urls')),


    # Health
    url(r"^health/", include("health_check.urls")),
    # API
    path("api/", include("config.api_router")),
]
