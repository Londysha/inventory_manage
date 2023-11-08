from django.contrib import admin
from .models import   Category, Product, ProductComposition, ProductionOrder, ProductionOrderInput, \
                      ProductionOrderOutput, AbnormalProductionConsuming, ReturnedBackProduct, RawInventory,\
                      RawInventoryHistoryOutput, RawInventoryHistoryInput, MidInventory, MidInventoryHistory, \
                      FinishedInventory, FinishedInventoryHistoryInput, FinishedInventoryHistoryOutput, \
                      Customer, SalesOrder
            

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductComposition)
admin.site.register(ProductionOrder)
admin.site.register(ProductionOrderInput)
admin.site.register(ProductionOrderOutput)
admin.site.register(AbnormalProductionConsuming)
admin.site.register(ReturnedBackProduct)
admin.site.register(RawInventory)
admin.site.register(RawInventoryHistoryOutput)
admin.site.register(RawInventoryHistoryInput)
admin.site.register(MidInventory)
admin.site.register(MidInventoryHistory)
admin.site.register(FinishedInventory)
admin.site.register(FinishedInventoryHistoryInput)
admin.site.register(FinishedInventoryHistoryOutput)
admin.site.register(Customer)
admin.site.register(SalesOrder)





# Register all models here.


