from django.db import models

# Create your models here.
class NutritionInfo(models.Model):
    """Creates instance of Nutrition information


       Instance fields
       name -- Name of the nutrition info (example: weight)
       unit -- Unit of measurement for nutrition (example: g)
    """
    name = models.CharField(max_length=50,verbose_name="Name")
    unit = models.CharField(max_length=50,verbose_name="Unit")

    def __str__(self):
        return "{} {}".format(self.name,self.unit)

class Products(models.Model):
    """Create instance of Products


       Instance fields
       name -- Name of the Products
       description -- description of the product with 1000 char limit
       status -- boolean status to indicate product active or not.
    """
    name = models.CharField(max_length=200,verbose_name="Name")
    description = models.CharField(max_length=1000, verbose_name="Description")
    status = models.BooleanField(default=True,verbose_name="Active")

    def __str__(self):
        return self.name

class NutriDirectory(models.Model):
    """Create instance of NutriDirectory

       Instance fields
       prod_id -- FK to Product
       nutri_info_id -- FK to NutritionInfo
       value -- Float value for the NutritionInfo for a specific product.
    """
    prod_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    nutri_info_id = models.ForeignKey(NutritionInfo, on_delete=models.CASCADE)
    value = models.FloatField(verbose_name="Value")

    #create unique constraint for one product, only one value per nutritionInfo.
    class Meta:
        unique_together = ('prod_id', 'nutri_info_id',)

    def __str__(self):
        return "{} ({}): {:.2f}".format(self.nutri_info_id.name,
                                        self.nutri_info_id.unit,
                                        self.value)
