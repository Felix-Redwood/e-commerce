from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_cart(request):
    """Renders all the contents of the cart"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Adds a number of items to the cart"""
    quantity = int(request.POST.get("quantity"))
    print(quantity)
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    print(cart)
    request.session['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request, id):
    """Adjusts the contents of the cart"""

    quantity = int(request.POST.get("quantity"))
    cart = request.session.get('cart', {})
    print(quantity)
    print(cart)

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    request.session['cart'] = cart
    print(cart)
    return redirect(reverse('view_cart'))
