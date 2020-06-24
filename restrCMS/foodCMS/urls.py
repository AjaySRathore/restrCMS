from django.urls import path
from . import views

urlpatterns = [
    path('nutri-info-list/', views.NutritionInfoListView.as_view(),name='nutri-info-list'),
]
