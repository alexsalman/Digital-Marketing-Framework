from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.urlresolvers import reverse

class Company(models.Model):
    market_name = models.CharField(max_length=50, unique=True, verbose_name="Market Name ")
    unique_name = models.CharField(max_length=100, unique=True, verbose_name="Registered Name ")
    overview = models.TextField(null=True, verbose_name="Company Overview ")
    # It must be YYYY-MM-DD format
    founded_year = models.DateField(null=True, verbose_name="Year Founded ")
    # It should be in this format +16502506353
    phone_number = PhoneNumberField(verbose_name="Phone Number (Optional) ")
    email_address = models.EmailField(max_length=100, verbose_name="Email Address ")
    website_url = models.URLField(max_length=200, blank=True, verbose_name="Website URL (Optional) ")
    company_logo = models.ImageField(upload_to="company_logo/", null=True, verbose_name="Company Logo ")
    address_country = models.CharField(max_length=50, verbose_name="Country Name ")
    address_state = models.CharField(max_length=50, verbose_name="State / Province Name ")
    address_city = models.CharField(max_length=50, verbose_name="City Name ")
    address_zip = models.CharField(max_length=5, blank=True, verbose_name="ZIP Code (Optional) ")
    address_street = models.CharField(max_length=50, verbose_name="Street Name / Number ")
    address_postal = models.CharField(max_length=5, blank=True, verbose_name="Postal Address (Optional) ")
    # To be filled automatically
    posted_date = models.DateField(db_index=True, auto_now_add=True, verbose_name="Posted Date")

    def get_absolute_url(self):
        return reverse('loop:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return u'%s' % (self.market_name)

class Product(models.Model):
    company = models.ForeignKey(Company, verbose_name="Company Name ")
    product_name = models.CharField(max_length=50, verbose_name="Product Name ")
    product_type = models.CharField(max_length=50, blank=True, verbose_name="Product Type (Optional) ")
    product_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Product Price ")
    # It must be YYYY-MM-DD format
    product_madedate = models.DateField(null=True, blank=True, verbose_name="Product Made On (Optional) ")
    product_picture = models.FileField(null=True, blank=True, verbose_name="Product Picture (Optional) ")
    # To be filled automatically
    posted_date = models.DateField(db_index=True, auto_now_add=True, verbose_name="Posted Date")

    def __str__(self):
        return u'%s' % (self.product_name)

class Offer(models.Model):
    company = models.ForeignKey(Company, verbose_name="Company Name ")
    product = models.ForeignKey(Product, verbose_name="Product Name ")
    offer_name = models.CharField(max_length=50, verbose_name="Offer Name ")
    offer_info = models.TextField(null=True, verbose_name="Offer Description ")
    offer_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, verbose_name="Offer Price (Optional) ")
    # It must be YYYY-MM-DD format
    offer_ends = models.DateField(null=True, verbose_name="Offer Ends On ")
    offer_picture = models.FileField(null=True, blank=True, verbose_name="Offer Picture (Optional) ")
    # To be filled automatically
    posted_date = models.DateField(db_index=True, auto_now_add=True, verbose_name="Posted Date")

    def __str__(self):
        return u'%s' % (self.offer_name)

class Coupon(models.Model):
    company = models.ForeignKey(Company, verbose_name="Company Name ")
    product = models.ForeignKey(Product, verbose_name="Product Name ")
    coupon_name = models.CharField(max_length=50, verbose_name="Coupon Name ")
    coupon_info = models.TextField(null=True, verbose_name="Coupon Description ")
    # It must be YYYY-MM-DD format
    coupon_ends = models.DateField(null=True, verbose_name="Coupon Ends On ")
    coupon_picture = models.FileField(null=True, blank=True, verbose_name="Coupon Picture (Recommended) ")
    # To be filled automatically
    posted_date = models.DateField(db_index=True, auto_now_add=True, verbose_name="Posted Date")

    def __str__(self):
        return u'%s' % (self.coupon_name)

class Contest(models.Model):
    company = models.ForeignKey(Company, verbose_name="Company Name ")
    product = models.ForeignKey(Product, verbose_name="Product Name ")
    contest_name = models.CharField(max_length=50, verbose_name="Contest Name ")
    contest_info = models.TextField(null=True, verbose_name="Contest Description ")
    # It must be YYYY-MM-DD format
    contest_ends = models.DateField(null=True, verbose_name="Contest Ends On ")
    contest_picture = models.FileField(null=True, blank=True, verbose_name="Contest Picture (Optional) ")
    # To be filled automatically
    posted_date = models.DateField(db_index=True, auto_now_add=True, verbose_name="Posted Date")

    def __str__(self):
        return u'%s' % (self.contest_name)
