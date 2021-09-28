from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from . models import CommissionLog

def commissionpay_view(request, id):
    commission_payment_details = get_object_or_404(CommissionLog, id=id)

    print(commission_payment_details.sales_person.sales_person)
    print(commission_payment_details.commission_amt)
    print(commission_payment_details.sales_person.order_amount)

    return HttpResponse('<html><body>Test Page for Commission Payment</body></html>')