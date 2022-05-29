from rest_framework import serializers
from django.core.cache import cache


class InMemorySerializer(serializers.Serializer):
    data = serializers.DictField()

    def create(self, validated_data):
        for key in validated_data.get('data'):
            stores = cache.set(key, validated_data.get('data').get(key))
            print(cache.get(key))

            return stores

class InMemorySearchSerializer(serializers.Serializer):
    prefix = serializers.CharField(required=False)
    suffix = serializers.CharField(required=False)

    def get_prefix(self, obj):
        if 'prefix' in obj:
            obj.startswith = obj.get('prefix')
            return cache.get(obj.get('prefix'))

    def get_suffix(self, obj):
        if 'suffix' in obj:
            obj.endswith = obj.get('suffix')
            return cache.get(obj.get('suffix'))


class InMemoryRetriveSerializer(serializers.Serializer):

    def create(self, validated_data, key):
        return cache.get(key)





