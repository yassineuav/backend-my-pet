from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_list),
    path('post/<int:id>/', views.post_detail),
    path('product/', views.ProductList.as_view()),
    path('product/<int:id>/', views.ProductList.as_view()),
    path('collections/', views.collection_list),
    path('collections/<int:pk>/', views.collection_detail),
]