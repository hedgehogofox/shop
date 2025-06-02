from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop_app.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from orders.models import OrderItem
from orders.forms import OrderCreateForm
from django.urls import reverse


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    quantity = int(request.POST.get('quantity', 1))
    category = request.POST.get('category')
    q = request.POST.get('q')
    cart.add(product=product,
                     quantity=quantity,
                     update_quantity=True)
    if category=="Деталь":
        url_with_id= reverse("shop_app:product_detail",
                                    kwargs={'id': product_id,
                                            'slug': product.slug})
    elif category=="Ванны":
        url= reverse("shop_app:product_list_by_category",
                                    kwargs={'category_slug': 'bath'})
        url_with_id = f"{url}#item_{product_id}"
    elif category=="Санфаянс":
        url= reverse("shop_app:product_list_by_category",
                                    kwargs={'category_slug': 'sanfayance'})
        url_with_id = f"{url}#item_{product_id}"
    elif category=="Кухонные":
        url= reverse("shop_app:product_list_by_category",
                                    kwargs={'category_slug': 'sink'})
        url_with_id = f"{url}#item_{product_id}"
    elif category=="Аксессуары":
        url= reverse("shop_app:product_list_by_category",
                                    kwargs={'category_slug': 'bathroom_accessories'})
        url_with_id = f"{url}#item_{product_id}"
    elif category=="Мебель":
        url= reverse("shop_app:product_list_by_category",
                                    kwargs={'category_slug': 'furniture'})
        url_with_id = f"{url}#item_{product_id}"
    elif category=="Смесители":
        url= reverse("shop_app:product_list_by_category",
                                    kwargs={'category_slug': 'faucet'})
        url_with_id = f"{url}#item_{product_id}"
    elif category=="Полотенцесушители":
        url= reverse("shop_app:product_list_by_category",
                                    kwargs={'category_slug': 'towel_rail'})
        url_with_id = f"{url}#item_{product_id}"
    elif category=="Инженерная":
        url= reverse("shop_app:product_list_by_category",
                                    kwargs={'category_slug': 'plumbing'})
        url_with_id = f"{url}#item_{product_id}"
    elif q:
        url= reverse("shop_app:search_results")
        url_with_id = f"{url}?q={q}#item_{product_id}"
    else:
        url= reverse("cart:cart_detail")
        url_with_id = f"{url}#item_{product_id}"
    return redirect(url_with_id)
    

def cart_add_one(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product,
             quantity=1,
             update_quantity=True)
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            form = OrderCreateForm
            return render(request, 'cart/detail.html',
                          {'order': order, 'form': form})
    else:
        form = OrderCreateForm
    return render(request, 'cart/detail.html', {'cart': cart, 'form': form})
