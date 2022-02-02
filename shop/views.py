from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


def shop(request):
    category=Category.objects.all()
    brands=Brand.objects.all()
    brandsID=request.GET.get('brands')
    categoryID=request.GET.get('category')
    if categoryID:
        product=Product.objects.filter(sub_category=categoryID).order_by('-id')
    elif brandsID:
        product=Product.objects.filter(brands=brandsID).order_by('-id')

    else:
        product=Product.objects.all()    
    context={
       'category':category,
       'product':product,
       'brands':brands,
        }


    return render(request,'index.html',context)


@login_required(login_url="/accounts/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("shop")


@login_required(login_url="/accounts/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')


def Contact_Page(request):
    if request.method == 'POST':
        contact=Contact_us(
            name= request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
            )
        contact.save()

    return render(request,'contact.html')


def Product_view(request):
    category=Category.objects.all()
    brands=Brand.objects.all()
    brandsID=request.GET.get('brands')
    categoryID=request.GET.get('category')
    if categoryID:
        product=Product.objects.filter(sub_category=categoryID).order_by('-id')
    elif brandsID:
        product=Product.objects.filter(brands=brandsID).order_by('-id')

    else:
        product=Product.objects.all()    
    context={
       'category':category,
       'product':product,
       'brands':brands,
        }
    return render(request,'product.html',context)


def Product_Detail(request,id):
    product=Product.objects.filter(id = id).first()
    context={
        'product':product,
    }
    return render(request,'product_detail.html',context)

def Search(request):
    query=request.GET['query']
    product=Product.objects.filter(name__icontains=query)
    context={
       'product':product
    }
    return render(request,'search.html',context)    