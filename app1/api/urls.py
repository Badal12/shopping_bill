from django.urls import path,include
from rest_framework import urlpatterns
from app1.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('customer/<int:pk>', views.CustomerViewset, basename='customer'),
router.register('product<int:pk>/', views.ProductViewset, basename='product'),
router.register('cart', views.CartViewset, basename='cart'),
router.register('orderplaced', views.OrderPlacedViewset, basename='orderplaced'),

urlpatterns = [
    path('',include(router.urls)),
]
#now link the above api url to the django url.py of project
#path('api/', include(app1.api.urls))
"for student model api is ready and you can perform the CRUD operations"