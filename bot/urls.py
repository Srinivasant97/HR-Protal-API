from django.contrib import admin
from django.urls import path,include
from .views import AnswerQuestions

urlpatterns = [
    path('quesions/',AnswerQuestions.as_view(),name='answer')
]
