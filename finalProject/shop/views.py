from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views import View


from .models import Product, Category, Order, OrderStatusChoice


def get_product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}

    return render(request, "shop/product_detail.html",context)


def get_categories(request):
    categories = Category.objects.all()
    ctx = {"categories": categories}

    return render(request, "shop/category_list.html", context=ctx)


class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'shop/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category = self.get_object())
        return context


@login_required(login_url="/users/login")
def order_add(request, id):
    user = request.user
    order, created = Order.objects.get_or_create(customer=user, status=OrderStatusChoice.INITIAL)
    product = Product.objects.get(id=id)
    # order.product_set.add(product)
    if "add_product_to_basket" in request.POST:
        order.product_set.add(product)

    return redirect("home")

@login_required(login_url="/users/login")
def order_detail(request):
    order = Order.objects.all()
    ctx = {"order": order}

    return render(request, "shop/basket.html", context=ctx)



# @login_required(login_url="/users/login")
# def item_clear(request, id):
#     cart = Order(request)
#     product = Product.objects.get(id=id)
#     cart.remove(product)
#     return redirect("cart_detail")
# #
#
# @login_required(login_url="/users/login")
# def item_increment(request, id):
#     cart = Cart(request)
#     product = Product.objects.get(id=id)
#     cart.add(product=product)
#     return redirect("cart_detail")
#
#
# @login_required(login_url="/users/login")
# def item_decrement(request, id):
#     cart = Cart(request)
#     product = Product.objects.get(id=id)
#     cart.decrement(product=product)
#     return redirect("cart_detail")
#
#
# @login_required(login_url="/users/login")
# def cart_clear(request):
#     cart = Cart(request)
#     cart.clear()
#     return redirect("cart_detail")
#
#













