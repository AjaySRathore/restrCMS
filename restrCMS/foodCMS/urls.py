from django.urls import path
from . import views

urlpatterns = [
    path('nutri-info-list/', views.NutritionInfoListView.as_view(),
        name='nutri-info-list'),
    path('nutri-details/<int:pk>',views.NutritionInfoDetailView.as_view(),name="nutri-details"),

]
