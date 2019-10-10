from django.urls import path
from shop import views

urlpatterns = [
    path('products/', views.ProductView.as_view()),
    path('products/<int:pk>', views.ProductDetailViews.as_view()),
    path('products/category/', views.CategoryView.as_view()),
    path('products/category/<int:pk>', views.CategoryDetailViews.as_view()),
    path('auth/signup', views.CreateUserView.as_view()),
]
