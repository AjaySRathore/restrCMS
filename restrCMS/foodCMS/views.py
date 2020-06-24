from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView
from django.urls import reverse

from foodCMS.models import NutritionInfo,NutriDirectory,Products

@method_decorator(login_required, name="dispatch")
class NutritionInfoListView(ListView):
    model = NutritionInfo
    template_name = 'foodCMS/nutritionInfolist.html'

@method_decorator(login_required, name="dispatch")
class NutritionInfoDetailView(DetailView):
    model = NutritionInfo
    template_name = 'foodCMS/nutrition/nutritionDetailView.html'

@method_decorator(login_required, name="dispatch")
class NutritionInfoCreateView(CreateView):
    model = NutritionInfo
    fields = ['name','unit']
    template_name = 'foodCMS/nutrition/nutrition_create_form.html'

    def get_success_url(self):
        return reverse('nutri-details', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name="dispatch")
class NutritionInfoUpdateView(UpdateView):
    model = NutritionInfo
    fields = ['name','unit']
    template_name = 'foodCMS/nutrition/nutrition_update_form.html'

    def get_success_url(self):
        return reverse('nutri-details', kwargs={'pk': self.object.pk})
