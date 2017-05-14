from django.contrib import admin
from .models import Company, Product, Offer, Coupon, Contest

# Classes for presenting the admin page
class Company_Admin(admin.ModelAdmin):
    list_display = ('market_name', 'founded_year', 'email_address')
    search_fields = ('market_name',)
    list_filter = ('posted_date',)
    ordering = ('-posted_date',)

class Product_Admin(admin.ModelAdmin):
    list_display = ('company', 'product_name', 'product_price')
    search_fields = ('product_name',)
    list_filter = ('posted_date',)
    date_hierarchy = 'product_madedate'
    ordering = ('-posted_date',)

class Offer_Admin(admin.ModelAdmin):
    list_display = ('company', 'product', 'offer_name', 'offer_ends')
    search_fields = ('offer_name',)
    list_filter = ('posted_date',)
    date_hierarchy = 'offer_ends'
    ordering = ('-posted_date',)

class Coupon_Admin(admin.ModelAdmin):
    list_display = ('company', 'product', 'coupon_name', 'coupon_ends')
    search_fields = ('coupon_name',)
    list_filter = ('posted_date',)
    date_hierarchy = 'coupon_ends'
    ordering = ('-posted_date',)

class Contest_Admin(admin.ModelAdmin):
    list_display = ('company', 'product', 'contest_name', 'contest_ends')
    search_fields = ('contest_name',)
    list_filter = ('posted_date',)
    date_hierarchy = 'contest_ends'
    ordering = ('-posted_date',)

# Models of the loop
admin.site.register(Company, Company_Admin)
admin.site.register(Product, Product_Admin)
admin.site.register(Offer, Offer_Admin)
admin.site.register(Coupon, Coupon_Admin)
admin.site.register(Contest, Contest_Admin)
