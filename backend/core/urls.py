from django.urls import path
from .views import *


urlpatterns = [
    path('register/', UserRegistrationCreateView.as_view(), name='register'),
    path('profile/<slug:slug>/', UserRetrieveUpdateDestroyView.as_view(), name='profile'),
    path('specialist/', SpecialistListView.as_view(), name='specialist'),
    path('list_questions/', List_QuestionsListView.as_view(), name='list_questions')
    ]