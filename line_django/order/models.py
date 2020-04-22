from django.db import models

class Branch(models.Model):
    branch_code = models.CharField(db_column='branch_code',max_length=50)
    branch_id   = models.CharField(db_column='branch_id',max_length=50, unique=True)
    branch_name = models.CharField(db_column='branch_name',max_length=50)
    def __str__(self):
        return self.branch_name

class Product(models.Model):
    product_id       = models.CharField(db_column='product_id',max_length=10)
    product_name     = models.CharField(db_column='product_name',max_length=50, unique=True)
    product_type     = models.CharField(db_column='product_type',max_length=50, default='')
    product_size     = models.CharField(db_column='product_size',max_length=50, default='')
    product_group    = models.CharField(db_column='product_group',max_length=50)
    product_category = models.CharField(db_column='product_category',max_length=50)
    product_Image    = models.CharField(db_column='product_image',max_length=50,default='', blank=True)
    product_price    = models.FloatField(db_column='product_price',default=0)

    def __str__(self):
        return self.product_name + ' ' + self.product_type + ' ' + self.product_size

class Member(models.Model):
    member_id      = models.CharField(db_column='MEMBER_ID_C',max_length=50)
    member_name    = models.CharField(db_column='LASTNAME',max_length=50)
    mobile         = models.CharField(db_column='PERSONMOBILEPHONE',max_length=50)
    branch_1       = models.CharField(db_column='FAVORITE_BRANCH_1_C',max_length=50)
    branch_2       = models.CharField(db_column='FAVORITE_BRANCH_2_C',max_length=50)
    branch_3       = models.CharField(db_column='FAVORITE_BRANCH_3_C',max_length=50)
    favorite_drink = models.ForeignKey(Product,to_field='product_name', db_column='FAVORITE_DRINK_C', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.member_name

class CartItem(models.Model):
    product        = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True,)
    #cart           = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity       = models.IntegerField(default=0)
    #subtotal_price = models.FloatField()

    def __str__(self):
        return self.product.product_name+' item'

    def get_subtotal_price(self):
        return self.quantity * self.product.product_price

class Cart(models.Model):
    cart_id             = models.CharField(max_length=10)
    branch              = models.ForeignKey(Branch, on_delete=models.DO_NOTHING, null=True, blank=True)
    #items = models.ManyToManyField(CartItem)
    #total_price         = models.FloatField(default=0)
    cart_state          = models.BooleanField(default=False)
    cart_created_date   = models.DateTimeField()
    cart_expirated_date = models.DateTimeField()
    delivery_address    = models.CharField(max_length=50,default='')
    mobile              = models.CharField(max_length=10)

    def __str__(self):
        return self.mobile

    def get_total_price(self):
        total = 0
        for item in self.items.all():
            total += self.item.get_subtotal_price()
        return total
