from django.contrib import admin
from .models import name,User,product,categories,order,signup
# Register your models here.
admin.site.register(name)
admin.site.register(User)
admin.site.register(product)
admin.site.register(order)
admin.site.register(categories)
admin.site.register(signup)
