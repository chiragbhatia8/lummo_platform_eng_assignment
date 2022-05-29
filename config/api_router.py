# django imports
from django.urls import re_path, include

app_name = "api"

api_urls = [
    re_path(
        r"(?P<version>(v1))/",
        include(("app.lummo.urls", "lummo"), namespace="lummo"),
    )
]

urlpatterns = api_urls
