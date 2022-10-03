from django.contrib import admin
from django.urls import path
from inventarioApp.views.purchase.purchaseViewSet import PurchaseViewSet
from inventarioApp.views.product.productViewSet import ProductViewSet
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from inventarioApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('purchase/list',PurchaseViewSet.as_view({'get':'list'})),
    path('product/list',ProductViewSet.as_view({'get':'list'})),

    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('client/', views.ClientCreateView.as_view()),
    path('client/<int:pk>/', views.ClientDetailView.as_view()),
]
