from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArrendamientoViewSet, login, register, logout, arrendamientos

router = DefaultRouter()
router.register(r'arrendamientos', ArrendamientoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('arrendamientos/', arrendamientos, name='arrendamientos'),
]
