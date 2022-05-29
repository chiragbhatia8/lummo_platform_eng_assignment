from django.urls import path
from app.lummo.api.api_v1 import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
urlpatterns = [
    path("set",
        views.MemoryView.as_view(),
        name="cache_set",
        ),
    path("search",
        views.MemorySearchView.as_view(),
        name="cache_get",
        ),
    path("get/<str:key>",
        views.MemoryRetrieveView.as_view(),
        name="cache_retrieve",
        ),
]