
from rest_framework import views, response

from django.core.cache import cache

from app.lummo.api.api_v1.serializer import InMemorySerializer, InMemorySearchSerializer, InMemoryRetriveSerializer

class MemoryView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = InMemorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return response.Response(serializer.data)

class MemorySearchView(views.APIView):
    def get(self, request, *args, **kwargs):
        serializer = InMemorySearchSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        prefix = request.query_params.get('prefix')
        suffix = request.query_params.get('suffix')
        if prefix and suffix:
            return response.Response(cache.get(prefix + suffix))
        elif prefix:
            if prefix.startswith == prefix:
                return response.Response(cache.get(prefix))
            else:
                return response.Response(cache.get(prefix))
        elif suffix:
            return response.Response(cache.get(suffix))
        else:
            return response.Response("No data")


class MemoryRetrieveView(views.APIView):
    def get(self, request, *args, **kwargs):
        serializer = InMemoryRetriveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return response.Response(cache.get(serializer.validated_data.get('data')))