from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_list),
    path('post/<int:id>/', views.post_detail),
]