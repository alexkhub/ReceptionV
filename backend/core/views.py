from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import *
from .permissions import *
from .serializers import *


class UserRegistrationCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'slug'
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options', 'trace']
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = [IsAuthenticated, UserObjectPermission]
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'profile': serializer.data}, status=status.HTTP_200_OK)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpecialistListView(ListAPIView):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'specialist': serializer.data}, status=status.HTTP_200_OK)



class  List_QuestionsListView(ListAPIView):
    queryset = List_Questions.objects.all()
    serializer_class = List_QuestionsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'list_question': serializer.data}, status=status.HTTP_200_OK)