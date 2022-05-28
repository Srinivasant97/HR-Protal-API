from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('hire/', include('hiring.urls')),
    path('task/', include('tasks.urls')),
    path('admin/', admin.site.urls),
]
