from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
#     PaymentView,
    AddCouponView,
    RequestRefundView,
    Shop,
    search,
    Shop_az,
    Shop_n,
    Shop_ph,
    Shop_pl,
    Shop_za,
    Shop_o
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search', search, name='search'),
    path('shop', Shop, name='shop'),

    path('shop_za', Shop_za, name='shop_za'),
    path('shop_az', Shop_az, name='shop_az'),
    path('shop_ph', Shop_ph, name='shop_ph'),
    path('shop_pl', Shop_pl, name='shop_pl'),
    path('shop_n', Shop_n, name='shop_n'),
    path('shop_o', Shop_o, name='shop_o'),



    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
#     path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]
