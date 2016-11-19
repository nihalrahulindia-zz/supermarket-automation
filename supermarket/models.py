from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible  # only if you need to support Python 2
class CustomerDB_Master(models.Model):
    Cust_ID = models.AutoField(db_column = 'Cust_ID', primary_key = True)
    Cust_Name = models.CharField(max_length = 200, db_column = 'Cust_name')
    Tel_No = models.CharField(max_length = 10, db_column = 'Tel_No', unique = True)
    Email = models.CharField(max_length = 200, db_column = 'Email', unique = True)

    def updateDB(self):
        self.save()

    def __str__(self):
        return self.Cust_Name

@python_2_unicode_compatible  # only if you need to support Python 2
class ProductDB_Master(models.Model):
    Prod_ID = models.AutoField(db_column = 'Prod_ID', primary_key = True)
    Prod_Name = models.CharField(max_length = 200, db_column = 'Prod_Name', unique = True)
    Real_Price_ToCompany = models.DecimalField(db_column = 'Real_Price_ToCompany', max_digits = 10, decimal_places = 2)
    Marked_Price_OnProduct = models.DecimalField(db_column = 'Marked_Price_OnProduct', max_digits = 10, decimal_places = 2)
    Selling_Price_ToCustomer = models.DecimalField(db_column = 'Selling_Price_ToCustomer', max_digits = 10, decimal_places = 2)
    Items_In_Inventory = models.IntegerField(db_column = 'Items_In_Inventory')

    def updateDB(self):
        self.save()

    def __str__(self):
        return self.Prod_Name

@python_2_unicode_compatible  # only if you need to support Python 2
class TransactionDB_Master(models.Model):
    Transaction_ID = models.AutoField(db_column = 'Transaction_ID', primary_key = True)
    Cust_ID = models.IntegerField(db_column = 'Cust_ID')
    Date_Of_Purchase = models.DateField(auto_now_add = True, db_column = 'Date_Of_Purchase')
    Time_Of_Purchase = models.TimeField(auto_now_add = True, db_column = 'Time_Of_Purchase')

    def getID(self):
        return self.Transaction_ID

    def updateDB(self):
        self.save()

    def __str__(self):
        return str(self.Transaction_ID)

@python_2_unicode_compatible  # only if you need to support Python 2
class TransactionSupportDB_Master(models.Model):
    ID = models.AutoField(db_column = 'ID', primary_key = True)
    Transaction_ID = models.IntegerField(db_column = 'Transaction_ID')
    Prod_ID = models.IntegerField(db_column = 'Prod_ID')
    Real_Price_ToCompany = models.DecimalField(db_column = 'Real_Price_ToCompany', max_digits = 10, decimal_places = 2)
    Selling_Price_ToCustomer = models.DecimalField(db_column = 'Selling_Price_ToCustomer', max_digits = 10, decimal_places = 2)
    Quantity_Purchased = models.IntegerField(db_column = 'Quantity_Purchased', default = 1)
    Profit_Loss = models.DecimalField(db_column = 'Profit_Loss', max_digits = 10, decimal_places = 2)

    def getID(self):
        return self.ID

    def updateDB(self):
        self.save()

    def __str__(self):
        return str(self.ID)
