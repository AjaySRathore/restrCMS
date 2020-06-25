from django.urls import path
from . import views

urlpatterns = [
    path('nutri-info-list/', views.NutritionInfoListView.as_view(),
        name='nutri-info-list'),
    path('nutri-details/<int:pk>',views.NutritionInfoDetailView.as_view(),
        name="nutri-details"),
    path('nutri-details/create',views.NutritionInfoCreateView.as_view(),
        name="nutri-create"),
    path('nutri-details/update/<int:pk>',views.NutritionInfoUpdateView.as_view(),
        name="nutri-update"),
    path('nutri-details/delete/<int:pk>',views.NutritionInfoDeleteView.as_view(),
        name="nutri-delete"),
    path('products-list/', views.ProductsListView.as_view(),
        name='products-list'),
    path('products/create',views.ProductsCreateView.as_view(),
        name="product-create"),
    path('products-details/<int:pk>',views.ProductsDetailView.as_view(),
        name="products-details"),
    path('products/delete/<int:pk>',views.ProductsDeleteView.as_view(),
        name="products-delete"),
    path('products/update/<int:pk>',views.ProductsUpdateView.as_view(),
        name="products-update"),
]
