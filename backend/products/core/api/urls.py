from django.urls import path

from products.core.api.v1.viewsets import (
    LoginViewSet,
    ProductViewSet,
    ProductDeleteViewSet,
    ProductUpdateViewSet,
)

app_name = 'products_api'

urlpatterns = [
    path('login', LoginViewSet.as_view(), name='login'),
    path('products', ProductViewSet.as_view(), name='products'),
    path('products/<int:pk>/update', ProductUpdateViewSet.as_view(), name='update'),
    path('products/<int:pk>/delete', ProductDeleteViewSet.as_view(), name='delete'),
    path('products/<int:pk>', ProductViewSet.as_view(), name='product'),
]
