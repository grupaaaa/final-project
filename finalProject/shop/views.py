from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin



from .models import Product, Category, Order, OrderStatusChoice, OrderItem


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
        context['products'] = Product.objects.filter(category=self.get_object())

        return context


#

# @login_required(login_url="/users/login")
# def order_add(request, id):
#     user = request.user
#     order, created = Order.objects.get_or_create(customer=user, status=OrderStatusChoice.INITIAL)
#     item = Product.objects.get(id=id)
#     # order.item_set.add(item)
#     if "add_product_to_basket" in request.POST:
#         order.item_set.add(item)
#
#     return redirect("home")

# @login_required(login_url="/users/login")
# def cart(request):
#     item = OrderItem.objects.all()
#     ctx = {"item": item}
#
#     return render(request, "shop/basket.html", context=ctx)

def cart(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(customer=user, status=OrderStatusChoice.INITIAL)
        items = order.orderitem_set.all()
    else:
        items = []

    context= {'items': items,
              'order': order}
    return render(request, 'shop/basket.html', context)

def checkout(request):
    context = {}
    return render(request, 'shop/checkout.html', context)


#
# # @login_required(login_url="/users/login")
# class OrderDetailView(LoginRequiredMixin,DetailView):
#     model = Product
#     context_object_name = 'product'
#     template_name = 'shop/checkout.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['orders'] = Order.objects.filter(product=self.get_object())
#
#         return context


# @login_required(login_url="/users/login")
# def update_order(request,id):
#     order=Order.objects.all()
#     try:
#         product=Product.objects.get(id=id)
#     except Product.DoesNotExist:
#         pass
#     if not product in order.products_set.all():
#         order.products_set.add(product)
#     else:
#         order.products_set.remove(product)
#     return HttpResponseRedirect("shop/basket.html")



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
class BreadAndBakingGoodsView(TemplateView):
    context_object_name = 'categories'
    template_name = "bread_and_baking_goods.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    # def context_category(self, **kwargs):
    #     context = super().get_context_category(**kwargs)
    #     context['products'] = Product.objects.filter(category=self.get_object())
    #
    #     return context


class DairyProductsView(TemplateView):
    context_object_name = 'categories'
    template_name = "dairy_products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class FruitAndVegetablesView(TemplateView):
    context_object_name = 'categories'
    template_name = "fruit_and_vegetables.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class JuicesAndDrinksView(TemplateView):
    context_object_name = 'categories'
    template_name = "juices_and_drinks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class MeatView(TemplateView):
    context_object_name = 'categories'
    template_name = "meat.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context



