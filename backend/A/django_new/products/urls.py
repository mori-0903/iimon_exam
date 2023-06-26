from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,product_list
from django.views.decorators.csrf import csrf_exempt

router = DefaultRouter()
router.register('', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('items/', product_list, name='product-list'),
]