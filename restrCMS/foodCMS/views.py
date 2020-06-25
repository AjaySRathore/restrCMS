from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView

from foodCMS.models import NutritionInfo,NutriDirectory,Products
from foodCMS.forms import *

@method_decorator(login_required, name="dispatch")
class IndexView(TemplateView):
    template_name = 'foodCMS/index.html'

@method_decorator(login_required, name="dispatch")
class NutritionInfoListView(ListView):
    model = NutritionInfo
    template_name = 'foodCMS/nutrition/nutritionInfolist.html'

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
    def get_queryset(self):
        status_filter = self.request.GET.get('status', 'none')
        name_filter = self.request.GET.get('name','none')
        if status_filter != 'none':
            context = Products.objects.filter(status=status_filter)
        elif name_filter != 'none':
            context = Products.objects.filter(name__icontains=name_filter)
        else:
            context = Products.objects.all()
        return context


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

@method_decorator(login_required, name="dispatch")
class ProductsDeleteView(DeleteView):
    model = Products
    template_name = 'foodCMS/products/product_confirm_delete.html'
    success_url = reverse_lazy("products-list")

@method_decorator(login_required, name="dispatch")
class ProductsUpdateView(UpdateView):
    model = Products
    form_class = ProductsForm
    template_name = 'foodCMS/products/product_update_form.html'

    def get_object(self, queryset=None):
        self.object = super(ProductsUpdateView, self).get_object()
        return self.object

    def get(self, request,*args,**kwargs):
        self.object = self.get_object()
        form= ProductsForm(instance=self.object)
        nutri_form = NutriDirectoryFormSet(instance=self.object)
        return self.render_to_response(
                                    self.get_context_data(
                                                form=form,
                                                nutri_form=nutri_form))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ProductsForm(data=self.request.POST,instance=self.object)
        nutri_form = NutriDirectoryFormSet(data=self.request.POST,instance=self.object)
        if form.is_valid():
            print('form is valid')
        if nutri_form.is_valid():
            print('nutri_form is valid')
        else:
            print(nutri_form)
        if (form.is_valid()):
            return self.form_valid(form,nutri_form)
        else:
            return self.form_invalid(form,nutri_form)

    def form_valid(self, form, nutri_form):
        self.object = form.save()
        nutri_form.instance = self.object
        nutri_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, nutri_form):
        return self.render_to_response(
            self.get_context_data(form=form, nutri_form=nutri_form))

    def get_success_url(self):
        return reverse('products-list')
