# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Order, OrderItem, Product
from ..serializers.order_serializers import OrderSerializer
from django.shortcuts import get_object_or_404

@api_view(["POST"])
def create_order(request):
    data = request.data

    order = Order.objects.create(
        full_name=data["full_name"],
        email=data["email"],
        address=data["address"],
        paid=False,
    )

    #Create OrderItems
    for item in data["items"]:
        product = get_object_or_404(Product, id=item["id"])
        OrderItem.objects.create(
            order=order,
            product=product,
            price=item["price"],
            quantity=item["qty"],
        )

    return Response({"message": "Order placed", "order_id": order.id})
