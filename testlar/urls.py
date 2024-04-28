from django.urls import path
from . import views

urlpatterns = [
    path('', views.TestsList.as_view(), name='tests_list'),
    path('<int:pk>/', views.TestDetail.as_view(), name='test_detail'),
    path('<int:pk>/update', views.TestUpdate.as_view(), name='test_update'),
    path('<int:pk>/delete', views.TestDetele.as_view(), name='test_delete'),
    path('create/', views.TestCreate.as_view(), name='test_create'),
    path('questions/', views.QuestionsList.as_view(), name='questions_list'),
    path('questions/<int:pk>/', views.QuestionDetail.as_view(), name='question_detail'),
    path('questions/<int:pk>/update', views.QuestionUpdate.as_view(), name='question_update'),
    path('questions/<int:pk>/delete', views.QuestionDetele.as_view(), name='question_delete'),
    path('questions/create/', views.QuestionCreate.as_view(), name='question_create'),
]