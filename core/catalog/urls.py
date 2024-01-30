from django.urls import path

from .views import ProductListView, CategoryListView

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('products/', ProductListView.as_view(), name='product_list'),
    
]