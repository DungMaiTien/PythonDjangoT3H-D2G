from django.shortcuts import render, redirect
from .models import CartItem
from django.contrib import messages

# Create your views here.
def cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart/cart.html',{'cart_items': cart_items, 'total_price': total_price})

def delete_cart_item(request, cart_item_id):
    try:
        cart_item = CartItem.objects.get(pk=cart_item_id)
        cart_item.delete()
        messages.success(request, "Sản phẩm đã bị xóa thành công.")
    except CartItem.DoesNotExist:
        messages.error(request, "Không thể tìm thấy sản phẩm trong giỏ hàng.")
    
    return redirect('cart:cart')