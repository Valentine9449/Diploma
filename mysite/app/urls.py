from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from . import views
from .views import SearchResultsView

app_name = 'station'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('prices/', views.prices, name='prices'),
    path('profile/', views.profile, name='profile'),
    path('about-us/', views.about_us, name='about_us'),


    path('sunline/', views.sunline, name='sunline'),
    path('catalog/<slug:post_slug>', views.about_product, name='about_product'),
    path('search/', views.SearchResultsView.as_view(), name='result'),
    path('stations/', views.stations, name='stations'),
    path('pumps/', views.pumps, name='pumps'),
    path('reservoirs/', views.reservoirs, name='reservoirs'),
    path('stationary-stations/', views.stationary_stations, name='stationary-stations'),
    path('delivery/', views.delivery, name='delivery'),
    path('service/', views.service, name='service'),

    path('comments/', views.comment, name='comment'),
    path('comments/delete/<int:pk>', views.admin_comment_delete, name='comment_delete'),


    path('catalog/cart/add/<slug:post_slug>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<slug:post_slug>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<slug:post_slug>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<slug:post_slug>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/complete/', views.cart_complete, name='cart_complete'),


    path('mail/', views.admin_mail, name='admin_mail'),
    path('mail/more/<int:pk>/', views.admin_more_mail, name='mail_more'),
    path('mail/delete/<int:pk>/', views.admin_mail_delete, name='mail_delete'),
    path('mail/accept/<int:pk>/', views.admin_mail_accept, name='mail_accept'),

    path('order/', views.admin_order, name='admin_order'),
    path('order/delete/<int:pk>/', views.admin_order_delete, name='order_delete'),
    path('order/accept/<int:pk>/', views.admin_order_accept, name='order_accept'),

]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)