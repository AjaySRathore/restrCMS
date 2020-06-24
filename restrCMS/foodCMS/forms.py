from django import forms
from django.forms.models import inlineformset_factory
from foodCMS.models import *

class ProductsForm(forms.ModelForm):

    class Meta:
        model = Products
        exclude = ()

class NutriDirectoryForm(forms.ModelForm):

    class Meta:
        model = NutriDirectory
        exclude = ()
#calculate length of NutritionInfo query set to decide how many rows should appear
NutriDirectoryFormSet = inlineformset_factory(
    Products, NutriDirectory, form=NutriDirectoryForm,
    fields=['nutri_info_id', 'value'],
    extra=len(NutritionInfo.objects.all()), 
    can_delete=False
    )
