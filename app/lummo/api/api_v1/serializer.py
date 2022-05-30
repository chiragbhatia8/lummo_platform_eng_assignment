
from rest_framework import serializers
from config.settings import redis


class InMemorySerializer(serializers.Serializer):
    data = serializers.DictField()

    def create(self, validated_data):

        for key in validated_data.get('data'):
            stores = redis.set(key, validated_data.get('data').get(key))

            return stores

class InMemoryRetriveSerializer(serializers.Serializer):

    def create(self, validated_data, key):
        return redis.get(key)





