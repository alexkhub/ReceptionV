from django.urls import path
from .views import *


urlpatterns = [
    path('register/', UserRegistrationCreateView.as_view(), name='register'),
    path('profile/<slug:slug>/', UserRetrieveUpdateDestroyView.as_view(), name='profile'),
    path('specialist/', SpecialistListView.as_view(), name='specialist'),
    path('list_questions/', List_QuestionsListView.as_view(), name='list_questions'),
    path('new_application/', ApplicationCreateView.as_view(), name='new_application'),
    path('my_application/', ApplicationListView.as_view(), name='my_application'),
    ]