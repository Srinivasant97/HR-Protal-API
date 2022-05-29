from django.urls import path

from . import views

from .views import (
    task, task_review, mine_block, get_chain, is_valid, add_transaction
)


urlpatterns = [
    path('task/<int:pk>', task),
    path('task_review/<int:pk>', task_review),
    path('mine_block', mine_block),
    path('get_chain', get_chain),
    path('is_valid', is_valid),
    path('add_transaction', add_transaction),
]
