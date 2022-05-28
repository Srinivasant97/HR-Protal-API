from django.db import models
from hiring.models import Employee

# Create your models here.


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_title = models.CharField(max_length=100)
    task_description = models.TextField(null=True)
    TASK_STATUS = (
        ('BACKLOG', 'BACKLOG'),
        ('IN_PROGRESS', 'IN_PROGRESS'),
        ('DONE', 'DONE'),
        ('TESTED', 'TESTED'),
        ('REJECTED', 'REJECTED'),
        ('ACCEPTED', 'ACCEPTED')
    )
    task_status = models.CharField(
        max_length=20, choices=TASK_STATUS, default='BACKLOG')
    task_created_on = models.DateTimeField(auto_now_add=True)
    task_updated_on = models.DateTimeField(auto_now=True)
    task_assigned_to = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='task_assigned_to', null=True)
    task_assigned_by = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='task_assigned_by', null=True)
    task_start_date = models.DateTimeField(null=True)
    task_end_date = models.DateTimeField(null=True)
    task_estimated_time = models.IntegerField(null=True)
    task_actual_time = models.IntegerField(null=True)
    task_priority = models.IntegerField(null=True)

    class Meta:
        db_table = 'task'


class TaskReview(models.Model):
    task_review_id = models.AutoField(primary_key=True)
    task_review_task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    task_review_emp_id = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='task_review_emp_id')
    task_review_rating = models.IntegerField(null=True)
    task_review_comment = models.TextField(null=True)
    task_review_created_on = models.DateTimeField(auto_now_add=True)
    task_review_updated_on = models.DateTimeField(auto_now=True)
    TASK_REVIEW_TYPE = (
        ('ANONYMOUS', 'ANONYMOUS'),
        ('PRIVATE', 'PRIVATE'),
        ('PUBLIC', 'PUBLIC'),
    )
    task_review_type = models.CharField(
        max_length=20, choices=TASK_REVIEW_TYPE, default='PUBLIC')

    class Meta:
        db_table = 'task_review'


class RewardCoins(models.Model):
    reward_coins_id = models.AutoField(primary_key=True)
    reward_coins_emp_id = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='reward_coins_emp_id')
    reward_coins_points = models.IntegerField()
    reward_coins_created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'reward_coins'
