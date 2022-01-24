from django.contrib import admin
from .models import name,User,product,category,order,signup
# Register your models here.
admin.site.register(name)
admin.site.register(User)
admin.site.register(product)
admin.site.register(order)
admin.site.register(category)
admin.site.register(signup)
