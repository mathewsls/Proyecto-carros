from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Arrendamiento
from .serializers import ArrendamientoSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@api_view(["POST", "GET"])
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)

@api_view(["POST", "GET"])
def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(serializer.data["password"])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)

class ArrendamientoViewSet(viewsets.ModelViewSet):
    queryset = Arrendamiento.objects.all()
    serializer_class = ArrendamientoSerializer

@login_required
def arrendamientos(request):
    arrendamientos = Arrendamiento.objects.all()
    return render(request, 'arrendamientos.html', {'arrendamientos': arrendamientos})
