from django.contrib import admin

from .models import Gas, Stock, PastStock, Category, Product, Service, Comment, Order


@admin.register(Gas)
class AdminGasPanel(admin.ModelAdmin):
    list_display = ('gas_name', 'gas_price', 'gas_type')
    
@admin.register(Order)
class AdminGasPanel(admin.ModelAdmin):
    list_display = ('user', 'price', 'name')


@admin.register(Stock)
class AdminStockPanel(admin.ModelAdmin):
    list_display = ('short_text', 'start_stock', 'end_stock')


@admin.register(PastStock)
class AdminStockPanel(admin.ModelAdmin):
    list_display = ('short_text', 'start_stock')


@admin.register(Category)
class AdminStockPanel(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class AdminStockPanel(admin.ModelAdmin):
    list_display = ('category', 'name')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Service)
class AdminGasPanel(admin.ModelAdmin):
    list_display = ('first_name', 'full_text', 'created')


@admin.register(Comment)
class AdminGasPanel(admin.ModelAdmin):
    list_display = ('user', 'comment_text', 'created')
