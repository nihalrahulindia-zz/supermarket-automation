from django.contrib import admin

from .models import CustomerDB_Master,ProductDB_Master,TransactionDB_Master,TransactionSupportDB_Master

admin.site.register(CustomerDB_Master)
admin.site.register(ProductDB_Master)
admin.site.register(TransactionDB_Master)
admin.site.register(TransactionSupportDB_Master)
