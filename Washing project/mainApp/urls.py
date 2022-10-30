from django.urls import path
from .views import UserApiView, WasherApiView, CarApiView, WashCompanyApiView, ServiceApiView, OrderApiView
urlpatterns = [
    #User get
    path('get/all/users/', UserApiView.as_view()),
    path('get/user/<int:user_id>/', UserApiView.as_view()),
    #User post
    path('post/user/', UserApiView.as_view()),
    #User put
    path('put/user/<int:pk>/', UserApiView.as_view()),
    #User patch
    path('patch/user/<int:pk>/', UserApiView.as_view()),
    #User delete
    path('delete/user/<int:pk>/', UserApiView.as_view()),

    #Car get
    path('get/all/cars/', CarApiView.as_view()),
    path('get/car/<int:car_id>/', CarApiView.as_view()),
    #Car post
    path('post/car/', CarApiView.as_view()),
    #Car put
    path('put/car/<int:pk>/', CarApiView.as_view()),
    #Car patch
    path('patch/car/<int:pk>/', CarApiView.as_view()),
    #Car delete
    path('delete/car/<int:pk>/', UserApiView.as_view()),


    #Washer get
    path('get/all/washers/', WasherApiView.as_view()),
    path('get/washer/<int:washer_id>/', WasherApiView.as_view()),
    #Washer post
    path('post/washer/', WasherApiView.as_view()),
    #Washer put
    path('put/washer/<int:pk>/', WasherApiView.as_view()),


    #WashCompany get
    path('get/all/washCompanys/', WashCompanyApiView.as_view()),
    path('get/washCompany/<int:washCompany_id>/', WashCompanyApiView.as_view()),
    #WashCompany post
    path('post/washCompany/', WashCompanyApiView.as_view()),
    #WashCompany put
    path('put/washCompany/<int:pk>/', WashCompanyApiView.as_view()),


    #Service get
    path('get/all/service/', ServiceApiView.as_view()),
    path('get/service/<int:service_id>/', ServiceApiView.as_view()),
    #Service post
    path('post/service/', ServiceApiView.as_view()),
    #Service put
    path('put/service/<int:pk>/', ServiceApiView.as_view()),


    #Order get
    path('get/all/order/', OrderApiView.as_view()),
    path('get/order/<int:order_id>/', OrderApiView.as_view()),
    #Order post
    path('post/order/', OrderApiView.as_view()),
    #Order put
    path('put/order/<int:pk>/', OrderApiView.as_view()),



]
