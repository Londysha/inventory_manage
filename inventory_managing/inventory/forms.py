from django import forms
from .models import   Category, Product, ProductComposition, ProductionOrder, ProductionOrderInput, \
                      ProductionOrderOutput, AbnormalProductionConsuming, ReturnedBackProduct, RawInventory,\
                      RawInventoryHistoryOutput, RawInventoryHistoryInput, MidInventory, MidInventoryHistory, \
                      FinishedInventory, FinishedInventoryHistoryInput, FinishedInventoryHistoryOutput, \
                      Customer, SalesOrder

#category form
class CategoryForm(forms.ModelForm):
    field_order = ['category_code',"category_name"]
    class Meta:
        model = Category
        fields = ['category_code',"category_name"]
        labels = {'category_code': "Category Code", "category_name": "Category Name"}