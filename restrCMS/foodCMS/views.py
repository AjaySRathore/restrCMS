from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView

from foodCMS.models import NutritionInfo,NutriDirectory,Products

@method_decorator(login_required, name="dispatch")
class NutritionInfoListView(ListView):
    model = NutritionInfo
    template_name = 'foodCMS/nutritionInfolist.html'
