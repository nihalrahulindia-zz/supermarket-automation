from django import forms

class ReceiptForm(forms.Form):
    customer_id = forms.IntegerField(label='Customer ID')
    product_id1 = forms.IntegerField(label='Product ID1')
    quantity1 = forms.IntegerField(label='Quantity1')
    product_id2 = forms.IntegerField(label='Product ID2')
    quantity2 = forms.IntegerField(label='Quantity2')
    product_id3 = forms.IntegerField(label='Product ID3')
    quantity3 = forms.IntegerField(label='Quantity3')

class Bill_Customer(forms.Form):
    cust_id = forms.IntegerField(label = 'Customer ID')
    cust_name = forms.CharField(max_length = 200,label = 'Customer Name')
    cust_telephone = forms.CharField(max_length = 10,label = 'Contact Number')
    transact_id = forms.IntegerField(label = 'Transaction ID')
    date_of_purchase = forms.DateField(label = 'Date of Purchase')
    time_of_purchase = forms.TimeField(label = 'Time of Purchase')

class Bill_Product(forms.Form):
    prod_id = forms.IntegerField(label = 'Product ID')
    prod_name = forms.CharField(max_length = 200,label = 'Product Name')
    marked_price = forms.DecimalField(label = 'MRP',max_digits = 10, decimal_places = 2)
    selling_price = forms.DecimalField(label = 'Your Price',max_digits = 10, decimal_places = 2)
    quantity = forms.IntegerField(label = 'Quantity')
    rate = forms.DecimalField(label = 'Rate',max_digits = 10, decimal_places = 2)

class UpdateInventoryForm(forms.Form):
    product_id = forms.IntegerField(label='Product ID')
    new_items = forms.IntegerField(label='New Items')

class ChangePriceForm(forms.Form):
    product_id = forms.IntegerField(label='Product ID')
    new_price = forms.DecimalField(label = 'New Price',max_digits = 10, decimal_places = 2)

class SalesStatisticsForm(forms.Form):
    product_id = forms.IntegerField(label='Product ID')
    start_date = forms.DateField(label='Start Date')
    end_date = forms.DateField(label='End Date')
