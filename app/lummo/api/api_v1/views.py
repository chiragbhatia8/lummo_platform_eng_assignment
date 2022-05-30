
from rest_framework import views, response

from app.lummo.api.api_v1.serializer import InMemorySerializer, InMemoryRetriveSerializer

from config.settings import redis
class MemoryView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = InMemorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return response.Response(serializer.data)

class MemorySearchView(views.APIView):
    def get(self, request, *args, **kwargs):
        prefix = request.query_params.get('prefix')
        suffix = request.query_params.get('suffix')

        if prefix:
            return response.Response(redis.keys(f"{prefix}*"))
        elif suffix:
            return response.Response(redis.keys(f"*{suffix}"))
        else:
            return response.Response("No data")


class MemoryRetrieveView(views.APIView):
    def get(self, request, *args, **kwargs):
        serializer = InMemoryRetriveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer = serializer.create(serializer.validated_data, self.kwargs.get('key'))
        return response.Response(serializer)