from django.urls import path
from . import views


urlpatterns = [
    path('<str:level>/', views.CategoryListView1.as_view(), name='category-list1'),
    path('<str:level>/<str:parent>/', views.CategoryListView2.as_view(), name='category-list2')
]