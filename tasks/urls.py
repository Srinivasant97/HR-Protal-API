from django.urls import path

from . import views

from .views import (
    task, task_review
)


urlpatterns = [
    path('task/<int:pk>', task),
    path('task_review/<int:pk>', task_review),

]
