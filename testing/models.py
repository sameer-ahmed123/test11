from django.db import models

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
class categories(models.Model):
    category =models.CharField(max_length=100)

    def __str__(self):
        return self.category



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
    product_category =models.ForeignKey(categories ,on_delete=models.CASCADE ,default=None)
    price =models.IntegerField(default=0)
    discription =models.CharField(max_length=500 ,default="")
    Image = models.ImageField(upload_to="upload/products/")
    def __str__(self):
        return self.product_name



class order(models.Model):
    coustomer =models.CharField(max_length=100)
    product =models.ForeignKey(product,on_delete=models.CASCADE)
    status=models.BooleanField()
    def __str__(self):
        return self.coustomer