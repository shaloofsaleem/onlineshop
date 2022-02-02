
from django.urls import path
from. import views

urlpatterns=[
    path('',views.shop,name='shop'),
    #add to cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'), 


    #Contact form
     path('contact_us',views.Contact_Page,name='contact_page'),


     #product page
     path('product/',views.Product_view,name='product'),

     #product detail
     path('product/<str:id>',views.Product_Detail,name='product_detail'),

     #searching
     path('search/',views.Search,name='search')
     
]