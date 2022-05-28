from .models import Task, TaskReview, RewardCoins

from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        task = Task.objects.create(**validated_data)
        return task


class TaskReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskReview
        fields = '__all__'

    def create(self, validated_data):
        task_review = TaskReview.objects.create(**validated_data)
        return task_review


class RewardCoinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardCoins
        fields = '__all__'

    def create(self, validated_data):
        reward_coins = RewardCoins.objects.create(**validated_data)
        return reward_coins
