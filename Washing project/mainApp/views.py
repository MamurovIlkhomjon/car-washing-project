from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import views, response
from rest_framework.response import Response
from .serializers import UserSerializer, WasherSerializer, CarSerializer, WashCompanySerializer, ServiceSerializer, OrderSerializer
from .models import User, Car, Washer, WashCompany, Service, Order

# Create your views here.
##
class UserApiView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id', None)
        if user_id:
            user_list = User.objects.filter(id=user_id)
            if user_list:
                user = user_list.values()
                return response.Response({'user': user})
            else:
                return response.Response({'user': f'{user_id} id dagi user yo\'q!!!'})

        users = User.objects.all()
        return response.Response({'users':users.values()})

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'User post':serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        serializer = UserSerializer(data=request.data, instance=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'User put':serializer.data})
    
    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        serializer = UserSerializer(data=request.data, instance=user, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'User patch':serializer.data})
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user_delete = User.objects.get(id=pk)
        user_delete.delete()
        return Response({'delete': 'delete'})


class CarApiView(APIView):
    def get(self, request, *args, **kwargs):
        car_id = kwargs.get('car_id', None)
        if car_id:
            car_list = Car.objects.filter(id=car_id)
            if car_list:
                car = car_list.values()
                return response.Response({'car': car})
            else:
                return response.Response({'car': f'{car_id} id dagi car yo\'q!!!'})

        cars = Car.objects.all()
        return response.Response({'cars':cars.values()})

    def post(self, request, *args, **kwargs):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Car post':serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        car = Car.objects.filter(pk=pk).first()
        serializer = CarSerializer(data=request.data, instance=car)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Car put':serializer.data})

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        car = Car.objects.filter(pk=pk).first()
        serializer = CarSerializer(data=request.data, instance=car, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Car patch':serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user_delete = Car.objects.get(id=pk)
        user_delete.delete()
        return Response({'delete': 'delete'})


class WasherApiView(APIView):
    def get(self, request, *args, **kwargs):
        washer_id = kwargs.get('washer_id', None)
        if washer_id:
            washer_list = Washer.objects.filter(id=washer_id)
            if washer_list:
                washer = washer_list.values()
                return response.Response({'washer': washer})
            else:
                return response.Response({'washer': f'{washer_id} id dagi washer yo\'q!!!'})

        washers = Washer.objects.all()
        return response.Response({'washers':washers.values()})

    def post(self, request, *args, **kwargs):
        serializer = WasherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Washer post':serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        washer = Washer.objects.filter(pk=pk).first()
        serializer = WasherSerializer(data=request.data, instance=washer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Washer put':serializer.data})
    
    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        washer = Washer.objects.filter(pk=pk).first()
        serializer = WasherSerializer(data=request.data, instance=washer, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Washer patch':serializer.data})


class WashCompanyApiView(APIView):
    def get(self, request, *args, **kwargs):
        washCompany_id = kwargs.get('washCompany_id', None)
        if washCompany_id:
            washCompany_list = WashCompany.objects.filter(id=washCompany_id)
            if washCompany_list:
                washCompany = washCompany_list.values()
                return response.Response({'washCompany': washCompany})
            else:
                return response.Response({'washer': f'{washCompany_id} id dagi washCompany yo\'q!!!'})

        washCompanys = WashCompany.objects.all()
        return response.Response({'washCompanys':washCompanys.values()})

    def post(self, request, *args, **kwargs):
        serializer = WashCompanySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'WashCompany post':serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = WashCompany.objects.filter(pk=pk).first()
        serializer = WashCompanySerializer(data=request.data, instance=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'WashCompany put':serializer.data})

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        washCompany = WashCompany.objects.filter(pk=pk).first()
        serializer = WashCompanySerializer(data=request.data, instance=washCompany, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'WashCompany patch':serializer.data})


class ServiceApiView(APIView):
    def get(self, request, *args, **kwargs):
        service_id = kwargs.get('service_id', None)
        if service_id:
            service_list = Service.objects.filter(id=service_id)
            if service_list:
                service = service_list.values()
                return response.Response({'service': service})
            else:
                return response.Response({'service': f'{service_id} id dagi service yo\'q!!!'})

        services = Service.objects.all()
        return response.Response({'services':services.values()})

    def post(self, request, *args, **kwargs):
        serializer = ServiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Service post':serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = Service.objects.filter(pk=pk).first()
        serializer = ServiceSerializer(data=request.data, instance=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Service put':serializer.data})

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        service = Service.objects.filter(pk=pk).first()
        serializer = ServiceSerializer(data=request.data, instance=service, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Service patch':serializer.data})


class OrderApiView(APIView):
    def get(self, request, *args, **kwargs):
        order_id = kwargs.get('order_id', None)
        if order_id:
            order_list = Order.objects.filter(id=order_id)
            if order_list:
                order = order_list.values()
                return response.Response({'order': order})
            else:
                return response.Response({'order': f'{order_id} id dagi order yo\'q!!!'})

        orders = Order.objects.all()
        return response.Response({'orders':orders.values()})

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print('oooorrrrrrrrr')
        serializer.save()
        return Response({'Order post':serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        print(pk)
        user = Order.objects.filter(pk=pk).first()
        serializer = OrderSerializer(data=request.data, instance=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Order put':serializer.data}) 

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        print('salom')
        order = Order.objects.filter(pk=pk).first()
        serializer = OrderSerializer(data=request.data, instance=order, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Order patch':serializer.data})      