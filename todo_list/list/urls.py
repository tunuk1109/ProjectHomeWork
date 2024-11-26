from .views import TaskViewSet
from django.urls import path

urlpatterns = [
    path('', TaskViewSet.as_view({'get': 'list', 'post':'create'}), name='title_list'),
    path('<int:pk>/', TaskViewSet.as_view({'get': 'retrieve',
                        'put': 'update', 'delete': 'destroy'}), name='title_detail')
]