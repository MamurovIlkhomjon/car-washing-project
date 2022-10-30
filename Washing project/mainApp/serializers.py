from rest_framework import serializers
from .models import User, WashCompany, Washer, Car, Service, Order
from rest_framework.validators import UniqueTogetherValidator

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    role = serializers.ChoiceField(choices = [('admin', 'admin'), ('owner', 'owner')])
    washcompany_id = serializers.IntegerField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.role = validated_data.get('role', instance.role)
        instance.washcompany_id = validated_data.get('washcompany_id', instance.washcompany_id)
        instance.save()
        return instance 

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['name', 'washcompany_id'],
            )
        ]


class CarSerializer(serializers.Serializer):
    car_model = serializers.CharField(max_length=100)
    car_number = serializers.CharField(max_length=100)
    owner_name = serializers.CharField(max_length=100)
    owner_phone = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.car_model = validated_data.get('car_model', instance.car_model)
        instance.car_number = validated_data.get('car_number', instance.car_number)
        instance.owner_name = validated_data.get('owner_name', instance.owner_name)
        instance.owner_phone = validated_data.get('owner_phone', instance.owner_phone)
        instance.save()
        return instance 

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=Car.objects.all(),
                fields=['car_model', 'owner_name', 'owner_phone'],
            )
        ]


class WasherSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    avatar = serializers.ImageField(required=False, allow_empty_file=True)
    is_active = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Washer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.price = validated_data.get('price', instance.price)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance 
    
    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=Washer.objects.all(),
                fields=['name', 'phone'],
            )
        ]


class WashCompanySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    avatar = serializers.ImageField(required=False, allow_empty_file=True)
    location = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return WashCompany.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance


class ServiceSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    time = serializers.DateTimeField(required=False)
    price = serializers.IntegerField()
    washcompany_id = serializers.IntegerField()

    def create(self, validated_data):
        return Service.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.time = validated_data.get('time', instance.time)
        instance.price = validated_data.get('price', instance.price)
        instance.washcompany_id = validated_data.get('washcompany_id', instance.washcompany_id)
        instance.save()
        return instance

    
class OrderSerializer(serializers.Serializer):
    service_id = serializers.IntegerField()
    washer_id = serializers.IntegerField()
    car_id = serializers.IntegerField()
    price = serializers.IntegerField()
    is_active =serializers.BooleanField(default=False)
    is_cancelled = serializers.BooleanField(default=False)
    date = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.service_id = validated_data.get('service_id', instance.service_id)
        instance.washer_id = validated_data.get('washer_id', instance.washer_id)
        instance.car_id = validated_data.get('car_id', instance.car_id)
        instance.price = validated_data.get('price', instance.price)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_cancelled = validated_data.get('is_cancelled', instance.is_cancelled)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance