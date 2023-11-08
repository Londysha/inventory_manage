from django.db import models

# neccesary models for the different inventories
#build a list of all models in this file


#build a category model of category codes and category names
class Category(models.Model):
    category_code = models.CharField(max_length=200)
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.category_code}: {self.category_name}"

#build a model of product codes, product names, and product descriptions
class Product(models.Model):
    product_code = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,  null=True, blank=True, related_name='products')
    date_created = models.DateTimeField(auto_now_add=True)
    #TODO: add editor field
    def __str__(self):
        return f"{self.product_code}: {self.product_name}, {self.product_description}"
    

#build a model of product compositions
class ProductComposition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='components')
    component = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='used_in_products')
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    #TODO: add editor field, optize for many to many
    def __str__(self):
        return f"{self.product}: {self.component}, {self.quantity}"

#add choices of product order status
PRODUCT_ORDER_STATUS_CHOICES = (
    ("ongoing", "ongoing"),
    ("finished", "finished"),
    ("alert", "alert"),
)


#build a model of production orders
class ProductionOrder(models.Model):
    #add a field for production order number, and set as primary key
    production_order_number = models.CharField(max_length=200, primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='production_orders')
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    #add a field for production order status
    status = models.CharField(max_length=200, choices=PRODUCT_ORDER_STATUS_CHOICES, default="ongoing")
        

    def __str__(self):
        return f"{self.product}: {self.quantity}"
    


#build a model of production order components get from the inventory
class ProductionOrderInput(models.Model):
    production_order = models.ForeignKey(ProductionOrder, on_delete=models.CASCADE, related_name='inputs')
    component = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='used_in_production_orders')    
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.production_order}: {self.component}, {self.quantity}"
    
#build a model of production order generated products
class ProductionOrderOutput(models.Model):
    production_order = models.ForeignKey(ProductionOrder, on_delete=models.CASCADE, related_name='outputs')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='generated_by_production_orders')
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.production_order}: {self.product}, {self.quantity}"

#build a model of abnormal production consumings
class AbnormalProductionConsuming(models.Model):
    production_order = models.ForeignKey(ProductionOrder, on_delete=models.CASCADE, related_name='abnormal_consumings')
    component = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='abnormally_consumed_in_production_orders')
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.production_order}: {self.component}, {self.quantity}"

#build a model of returned back products
class ReturnedBackProduct(models.Model):
    production_order = models.ForeignKey(ProductionOrder, on_delete=models.CASCADE, related_name='returned_products')
    component = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='returned_in_production_orders')
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.production_order}: {self.product}, {self.quantity}"

#build a model of raw inventory
class RawInventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='raw_inventories')
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product}: {self.quantity}"
    
#define the types of the actions in the rawinventoryhistory
INVENTORY_HISTORY_ACTION_CHOICES = (
    ("add", "add"),      
    ("return", "return"),
    ("consume", "consume"), 
    ("alert", "alert"),
)

#build a model of history of raw inventory changes
class RawInventoryHistoryOutput(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='raw_inventory_outputs')
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=200, choices=INVENTORY_HISTORY_ACTION_CHOICES[-2:], default="add")
    quantity_after_action = models.IntegerField()

    def __str__(self):
        return f"{self.product}: {self.quantity}"

#build a model of history of raw inventory input changes
class RawInventoryHistoryInput(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='raw_inventory_inputs')
    quantity = models.IntegerField()
    price = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=200, choices=INVENTORY_HISTORY_ACTION_CHOICES[:2], default="add")
    quantity_after_action = models.IntegerField()

    def __str__(self):
        return f"{self.product}: {self.quantity}"

#build mid-inventory models
class MidInventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='mid_inventories')
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product}: {self.quantity}"
    
#build a model of history of mid inventory changes
class MidInventoryHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='mid_inventory_histories')
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=200, choices=INVENTORY_HISTORY_ACTION_CHOICES, default="add")
    quantity_after_action = models.IntegerField()

    def __str__(self):
        return f"{self.product}: {self.quantity}"
    
#build a model of finished inventory
class FinishedInventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='finished_inventories')
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product}: {self.quantity}"
    
#build a model of history of finished inventory changes
class FinishedInventoryHistoryInput(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='finished_inventory_inputs')
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=200, choices=INVENTORY_HISTORY_ACTION_CHOICES, default="add")
    quantity_after_action = models.IntegerField()

    def __str__(self):
        return f"{self.product}: {self.quantity}"
    
#build a model of history of finished inventory output changes
class FinishedInventoryHistoryOutput(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='finished_inventory_outputs')
    quantity = models.IntegerField()
    price = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=200, choices=INVENTORY_HISTORY_ACTION_CHOICES, default="add")
    quantity_after_action = models.IntegerField()

    def __str__(self):
        return f"{self.product}: {self.quantity}"

#build a model of customer information
class Customer(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_address = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=200)
    customer_email = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.customer_name}: {self.customer_address}, {self.customer_phone}, {self.customer_email}"
    
#build a model of sales order
class SalesOrder(models.Model):
    sales_order_number = models.CharField(max_length=200, primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales_orders')
    quantity = models.IntegerField()
    price = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,  null=True, blank=True, related_name='sales_orders')
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=PRODUCT_ORDER_STATUS_CHOICES, default="ongoing")

    def __str__(self):
        return f"{self.sales_order_number}:{self.product}, {self.quantity}, {self.price}, {self.status}, {self.date_created}"
