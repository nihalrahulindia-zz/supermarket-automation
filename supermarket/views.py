from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render, render_to_response
from decimal import Decimal
from django.db.models import Sum

from .models import *
from .forms import *

def index(request):
    product_detail = ProductDB_Master.objects.order_by('Prod_ID')
    context = {'product_detail': product_detail}
    #print(product_detail)
    return render(request, 'supermarket/index.html', context)

def print(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            customer_id = request.POST.get('customer_id')
            product_id1 = request.POST.get('product_id1')
            product_id2 = request.POST.get('product_id2')
            product_id3 = request.POST.get('product_id3')
            quantity1 = request.POST.get('quantity1')
            quantity2 = request.POST.get('quantity2')
            quantity3 = request.POST.get('quantity3')

            prod1 = ProductDB_Master.objects.get(Prod_ID = product_id1)
            prod1.Items_In_Inventory = prod1.Items_In_Inventory - int(quantity1)
            prod1.save()

            prod2 = ProductDB_Master.objects.get(Prod_ID = product_id2)
            prod2.Items_In_Inventory = prod2.Items_In_Inventory - int(quantity2)
            prod2.save()

            prod3 = ProductDB_Master.objects.get(Prod_ID = product_id3)
            prod3.Items_In_Inventory = prod3.Items_In_Inventory - int(quantity3)
            prod3.save()

            transact = TransactionDB_Master(Cust_ID = customer_id)
            transact.save()
            transact_id = TransactionDB_Master.objects.latest('Transaction_ID')


            # transact_support_id = list()

            profit_loss1 = (int(quantity1)*prod1.Selling_Price_ToCustomer) - (int(quantity1)*prod1.Real_Price_ToCompany)
            transact_support1 = TransactionSupportDB_Master(Transaction_ID = transact_id.getID(),Prod_ID = product_id1,Quantity_Purchased = quantity1,Real_Price_ToCompany = prod1.Real_Price_ToCompany,Selling_Price_ToCustomer = prod1.Selling_Price_ToCustomer,Profit_Loss = profit_loss1)
            transact_support1.save()
            #transact_support_id.append(TransactionSupportDB_Master.objects.latest('ID'))
            x = transact_support1.getID()

            profit_loss2 = (int(quantity2)*prod2.Selling_Price_ToCustomer) - (int(quantity2)*prod2.Real_Price_ToCompany)
            transact_support2 = TransactionSupportDB_Master(Transaction_ID = transact_id.getID(),Prod_ID = product_id2,Quantity_Purchased = quantity2,Real_Price_ToCompany = prod2.Real_Price_ToCompany,Selling_Price_ToCustomer = prod2.Selling_Price_ToCustomer,Profit_Loss = profit_loss2)
            transact_support2.save()
            #transact_support_id.append(TransactionSupportDB_Master.objects.latest('ID'))
            y = transact_support2.getID()

            profit_loss3 = (int(quantity3)*prod3.Selling_Price_ToCustomer) - (int(quantity3)*prod3.Real_Price_ToCompany)
            transact_support3 = TransactionSupportDB_Master(Transaction_ID = transact_id.getID(),Prod_ID = product_id3,Quantity_Purchased = quantity3,Real_Price_ToCompany = prod3.Real_Price_ToCompany,Selling_Price_ToCustomer = prod3.Selling_Price_ToCustomer,Profit_Loss = profit_loss3)
            transact_support3.save()
            #transact_support_id.append(TransactionSupportDB_Master.objects.latest('ID'))
            z = transact_support3.getID()

            # cust_form = Bill_Customer()
            # prod_form = Bill_Product()
            # total = 0;

            customer = CustomerDB_Master.objects.get(Cust_ID = customer_id)
            transaction = TransactionDB_Master.objects.get(Transaction_ID = str(transact_id))
            transact_support1 = TransactionSupportDB_Master.objects.get(ID = x)
            transact_support2 = TransactionSupportDB_Master.objects.get(ID = y)
            transact_support3 = TransactionSupportDB_Master.objects.get(ID = z)
            product1 = ProductDB_Master.objects.get(Prod_ID = transact_support1.Prod_ID)
            product2 = ProductDB_Master.objects.get(Prod_ID = transact_support2.Prod_ID)
            product3 = ProductDB_Master.objects.get(Prod_ID = transact_support3.Prod_ID)

            a = transact_support1.Selling_Price_ToCustomer * transact_support1.Quantity_Purchased
            b = transact_support2.Selling_Price_ToCustomer * transact_support2.Quantity_Purchased
            c = transact_support3.Selling_Price_ToCustomer * transact_support3.Quantity_Purchased
            total = a + b + c
            # cust_form.cust_id = customer.Cust_ID
            # cust_form.cust_name = customer.Cust_Name
            # cust_form.cust_telephone = customer.Tel_No
            # cust_form.transact_id = transact.Transaction_ID
            # cust_form.date_of_purchase = transact.Date_Of_Purchase
            # cust_form.time_of_purchase = transact.Time_Of_Purchase

            # product_form_list = list()

            # for x in range(0,3):
            #     transact_support = TransactionSupportDB_Master.objects.get(ID = transact_support_id[x])
            #     product = ProductDB_Master.objects.get(Prod_ID = transact_support.Prod_ID)
            #     prod_form.prod_id = product.Prod_ID
            #     prod_form.prod_name = product.Prod_Name
            #     prod_form.marked_price = product.Marked_Price_OnProduct
            #     prod_form.selling_price = transact_support.Selling_Price_ToCustomer
            #     prod_form.quantity = transact_support.Quantity_Purchased
            #     prod_form.rate = (prod_form.quantity*prod_form.selling_price)
            #     total = total + prod_form.rate
            #     product_form_list.append(prod_form)

            #return HttpResponse(cust_form)
            return render(request,'supermarket/receipt.html',{'Total':total,'Customer':customer,'Transaction':transaction,'Product2':product2,'Product3':product3,'Product1':product1,'Transact_support1':transact_support1,'Transact_support2':transact_support2,'Transact_support3':transact_support3})
    else:
        form = ReceiptForm()
    return render(request, 'supermarket/print.html', {'form': form})

def update(request):
    if request.method == "POST":
        form = UpdateInventoryForm(request.POST)
        if form.is_valid():
            product_id = request.POST.get('product_id')
            new_item = request.POST.get('new_items')
            product = ProductDB_Master.objects.get(Prod_ID = product_id)
            product.Items_In_Inventory = product.Items_In_Inventory + int(new_item)
            product.save()
            return render(request,'supermarket/update_success.html',{'Product':product})

    else:
        form = UpdateInventoryForm()
    return render(request, 'supermarket/update.html', {'form': form})


    product_detail = ProductDB_Master.objects.order_by('Prod_ID')
    context = {'product_detail': product_detail}

    return render(request, 'supermarket/update.html', context)

def see(request):
    product_detail = ProductDB_Master.objects.order_by('Prod_ID')
    context = {'product_detail': product_detail}
    return render(request, 'supermarket/see.html', context)

def change(request):
    if request.method == "POST":
        form = ChangePriceForm(request.POST)
        if form.is_valid():
            product_id = request.POST.get('product_id')
            new_price = request.POST.get('new_price')
            product = ProductDB_Master.objects.get(Prod_ID = product_id)
            product.Selling_Price_ToCustomer = new_price
            product.save()
            return render(request,'supermarket/change_success.html',{'Product':product})

    else:
        form = ChangePriceForm()
    return render(request, 'supermarket/change.html', {'form': form})

def statistics(request):
    if request.method == "POST":
        form = SalesStatisticsForm(request.POST)
        if form.is_valid():
            product_id = request.POST.get('product_id')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            transaction = TransactionDB_Master.objects.filter(Date_Of_Purchase__gte = start_date).filter(Date_Of_Purchase__lte = end_date)

            sum_quantity,sum_profit_loss = 0,0

            for x in transaction:
                a = TransactionSupportDB_Master.objects.filter(Transaction_ID = x.Transaction_ID).filter(Prod_ID = product_id)
                for y in a:
                    sum_quantity = sum_quantity + int(y.Quantity_Purchased)
                    sum_profit_loss = sum_profit_loss + float(y.Profit_Loss)

            product = ProductDB_Master.objects.get(Prod_ID = product_id)
            return render(request,'supermarket/statistics_result.html',{'Product':product,'sum_quantity':sum_quantity,'sum_profit_loss':sum_profit_loss})

    else:
        form = SalesStatisticsForm()
    return render(request, 'supermarket/statistics.html', {'form': form})
