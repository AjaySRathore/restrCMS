from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse, reverse_lazy

from foodCMS.models import NutritionInfo,NutriDirectory,Products
from foodCMS.forms import *

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

@method_decorator(login_required, name="dispatch")
class NutritionInfoDeleteView(DeleteView):
    model = NutritionInfo
    template_name = 'foodCMS/nutrition/nutrition_confirm_delete.html'
    success_url = reverse_lazy("nutri-info-list")

@method_decorator(login_required, name="dispatch")
class ProductsCreateView(CreateView):
    form_class = ProductsForm
    template_name = 'foodCMS/products/product_create_form.html'

    def get(self, request,*args,**kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        nutri_form = NutriDirectoryFormSet()
        return self.render_to_response(
                                    self.get_context_data(form=form,
                                                nutri_form=nutri_form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        nutri_form = NutriDirectoryFormSet(self.request.POST)
        if (form.is_valid() and nutri_form.is_valid()):
            return self.form_valid(form,nutri_form)
        else:
            return self.form_invalid(form,nutri_form)

    def form_valid(self, form, nutri_form):
        self.object = form.save()
        nutri_form.instance = self.object
        nutri_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('products-list')

@method_decorator(login_required, name="dispatch")
class ProductsListView(ListView):
    model = Products
    template_name = 'foodCMS/products/prodcutslist.html'
    def get_context_data(self, **kwargs):
        kwargs = super(ProductsListView, self).get_context_data(**kwargs)
        nutri_directory = NutriDirectory.objects.all()
        kwargs.update({
            'nutri_directory': nutri_directory
        })
        return kwargs

@method_decorator(login_required, name="dispatch")
class ProductsDetailView(DetailView):
    model = Products
    template_name = 'foodCMS/products/productsDetailView.html'
    def get_context_data(self, **kwargs):
        kwargs = super(ProductsDetailView, self).get_context_data(**kwargs)
        nutri_directory = NutriDirectory.objects.filter(prod_id=self.get_object())
        kwargs.update({
            'nutri_directory': nutri_directory
        })
        return kwargs
