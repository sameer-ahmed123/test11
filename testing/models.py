from django.db import models
import datetime

# Create your models here.

#
# class login(models.Model):
#     Username=models.CharField(max_length=100)
#     Password=models.CharField(max_length=250)
#
#     class Meta:
#         db_table="login"

class signup(models.Model):
    Realname = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    sEmail = models.EmailField(max_length=150)
    sPassword = models.CharField(max_length=250)
    class Meta:
        db_table ="Signupusers"
    def __str__(self):
        return self.Realname

class name(models.Model):
    mName = models.CharField(max_length=100)
    class Meta:
        db_table = "MYNAME"
    def __str__(self):
        return self.mName


#model 1
class category(models.Model):
    name =models.CharField(max_length=100)

    @staticmethod
    def get_all_categories():
        return category.objects.all()

    def __str__(self):
        return self.name



class User(models.Model):
    user_name =models.CharField(max_length=100)
    user_email =models.EmailField(max_length=150)
    user_password =models.CharField(max_length=200)
    user_contact =models.CharField(max_length=20)
    user_addres =models.CharField(max_length=500,default="")
    def __str__(self):
        return self.user_name



class product(models.Model):
    product_name =models.CharField(max_length=100)
    product_category =models.ForeignKey(category ,on_delete=models.CASCADE ,default=1)
    price =models.IntegerField(default=0)
    discription =models.CharField(max_length=500 ,default="")
    Image = models.ImageField(upload_to="upload/products/")
    def __str__(self):
        return self.product_name

    @staticmethod
    def get_products_by_id(ids):
        return product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return product.objects.filter(product_category=category_id)
        else:
            return product.get_all_products();


class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=150)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=500)
    password=models.CharField(max_length=500)

    class Meta():
        db_table ="Customers2"

    def register(self):
        self.save()


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False



    def isExists(self):
        if Customer.objects.filter(email= self.email):
            return True

        return False





class order(models.Model):
    product = models.ForeignKey(product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=500, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return order.objects.filter(customer=customer_id).order_by('-date')



