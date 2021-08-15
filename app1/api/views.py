from app1.api.serializers import CustomerSerializer,ProductSerializer,CartSerializer, OrderPlacedSerializer
from rest_framework import serializers, viewsets
from app1.models import Customer,Product,Cart,OrderPlaced
#if you want to apply the security that if user is registerd and have id and pass then only can access the data import below
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = SessionAuthentication
    permission_classes = IsAuthenticatedOrReadOnly

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = SessionAuthentication
    permission_classes = IsAuthenticatedOrReadOnly

class CartViewset(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = SessionAuthentication
    permission_classes = IsAuthenticatedOrReadOnly

class OrderPlacedViewset(viewsets.ModelViewSet):
    queryset = OrderPlaced.objects.all()
    serializer_class = OrderPlacedSerializer
    authentication_classes = SessionAuthentication
    permission_classes = IsAuthenticatedOrReadOnly