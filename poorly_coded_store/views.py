from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    id_from_form = request.POST["price"]
    price_from_form = float(Product.objects.get(id = id_from_form).price)

    # On the checkout page, calculate and display the total charge for the most recent order    
    total_charge = quantity_from_form * price_from_form
    #ensure the total charge has 2 decimal places:
    total_charge = "{:.2f}".format(total_charge)

    current_order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)

    # # On the checkout page, calculate and display the total quantity of all orders combined
    # total_quantity = 0

    # # On the checkout page, calculate and display the total amount charged for all orders combined
    # total_amount_charged = 0

    # for order in Order.objects.all():
    #     total_quantity += order.quantity_ordered
    #     total_amount_charged += order.total_price

    # print("Charging credit card...")
    # context={
    #     "order" : current_order,

    #     "overall_qty" : total_quantity,

    #     "total_amount_charged" : total_amount_charged
    # }
    return redirect('/receipt')

def receipt(request):
    # quantity_from_form = int(request.POST["quantity"])
    # price_from_form = float(request.POST["price"])

    # # On the checkout page, calculate and display the total charge for the most recent order    
    # total_charge = quantity_from_form * price_from_form
    # #ensure the total charge has 2 decimal places:
    # total_charge = "{:.2f}".format(total_charge)

    current_order = Order.objects.last()

    # On the checkout page, calculate and display the total quantity of all orders combined
    total_quantity = 0

    # On the checkout page, calculate and display the total amount charged for all orders combined
    total_amount_charged = 0

    for order in Order.objects.all():
        total_quantity += order.quantity_ordered
        total_amount_charged += order.total_price

    # print("Charging credit card...")
    context={
        "order" : current_order,

        "overall_qty" : total_quantity,

        "total_amount_charged" : total_amount_charged
    }
    return render(request, "store/checkout.html", context)