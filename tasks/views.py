from .models import Task, TaskReview, RewardCoins

from rest_framework import serializers
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializers import TaskSerializer, TaskReviewSerializer, RewardCoinsSerializer
from hiring.serializers import EmployeeSerializer


@api_view(['POST', 'GET', 'PATCH'])
def task(request, pk):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        if pk and pk > 0:
            tasks = Task.objects.filter(task_id=pk)
        else:
            tasks = Task.objects.all()
        all_tasks = []
        for task in tasks:
            each_task = {
                ** TaskSerializer(task).data,
                'task_assigned_to': EmployeeSerializer(task.task_assigned_to).data,
                'task_assigned_by': EmployeeSerializer(task.task_assigned_by).data,
            }
            all_tasks.append(each_task)
        return Response(all_tasks, status=status.HTTP_200_OK)

    if request.method == 'PATCH':
        if pk and pk > 0:
            task = Task.objects.get(task_id=pk)
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET', 'PATCH'])
def task_review(request, pk):
    if request.method == 'POST':
        serializer = TaskReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        if pk and pk > 0:
            task_reviews = TaskReview.objects.filter(task_review_task_id=pk)
        else:
            task_reviews = TaskReview.objects.all()
        all_task_reviews = []
        for task_review in task_reviews:
            each_task_review = {
                ** TaskReviewSerializer(task_review).data,
                'task': TaskSerializer(task_review.task_review_task_id).data,
                'task_review_by': EmployeeSerializer(task_review.task_review_emp_id).data,
            }
            all_task_reviews.append(each_task_review)
        return Response(all_task_reviews, status=status.HTTP_200_OK)

    if request.method == 'PATCH':
        if pk and pk > 0:
            task_review = TaskReview.objects.get(task_review_id=pk)
            serializer = TaskReviewSerializer(task_review, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)
