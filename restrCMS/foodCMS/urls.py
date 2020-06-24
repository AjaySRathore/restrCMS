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
        name="nutri-delete")
]
