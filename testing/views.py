from django.shortcuts import render,redirect,HttpResponseRedirect
from testing.models import name,signup,product,category,Customer,order
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.views import View
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.

#                                           this is DJango auth login
# def login(request):
#     if request.method == "POST":
#         username =request.POST['lgusername']
#         password =request.POST['lgpassword']
#         user =auth.authenticate(username=username,password=password)
#
#         if user is not None:
#             auth.login(request,user)
#             return redirect("/")
#         else:
#             messages.info(request,"invalid username or password")
#             return redirect("/login")
#     else:
#         return render(request,"login.html")
#

# def signup1(request):                       this is Django auth signup
#         if request.method =="POST":
#             Realname= request.POST['realname']
#             Username= request.POST['username']
#             sEmail= request.POST['semail']
#             sPassword= request.POST['spassword']
#
#             if User.objects.filter(username=Username).exists():
#                 messages.info(request,"user exists")
#                 return redirect("/signup")
#             else:
#                 user= User.objects.create_user(username=Username,email=sEmail,password=sPassword,first_name=Realname)
#                 user.save()
#                 auth.login(request,user)
#                 print("user made")
#                 return redirect("/")
#
#         else:
#             form1 = signup.objects.all()
#             return render(request,'Signup.html',{'signup':form1})




#                                    this is django auth logout
# def logout(request):
#     auth.logout(request)
#     return redirect("/")



def show(request):
    Name= product.objects.all()
    return render(request,"show.html",{"Name":Name})
def edit(request,id):
    Name = product.objects.get(id=id)
    return render(request,'edit.html',{"Name":Name})


def destroy(request,id):
    Name= product.objects.get(id=id)
    Name.delete()
    return redirect('/')

class Index(View):


    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')



def store(request):
    categories = category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = product.get_all_products_by_categoryid(categoryID)
    else:
        products = product.get_all_products();

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'store.html', data)



class Signup(View):
    def get(self,request):
        return render(request,"signup.html")

    def post(self,request):
        postData =request.POST
        first_name =postData.get('firstname')
        last_name=postData.get('lastname')
        phone =postData.get('phone')
        email=postData.get('email')
        password=postData.get('password')

        #validate here
        value ={
            'first_name':first_name,
            'last_name':last_name,
            'phone':phone,
            'email':email
        }
        error_message =None

        customer=Customer(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=password
        )
        error_message=self.validateCustomer(customer)

        if not error_message:
            customer.password=make_password(customer.password)
            customer.register()
            return redirect('/signup')
        else:
            data={
                'error':error_message,
                'values':value
            }
            return render(request,'signup.html',data)

    def validateCustomer(self,customer):
        error_message =None;
        if not(customer.first_name):
            error_message="First name is requierd to enter"
        elif len(customer.first_name) <4:
            error_message=" First name must be 4 charecters or more"
        elif not(customer.last_name):
            error_message="Last name is reqied"
        elif len(customer.last_name) < 4:
            error_message="last name should be 4 charecters or more"
        elif not(customer.phone):
            error_message="please enter your phone"
        elif len(customer.phone) <11:
            error_message="phone number must be 11 charecters long"
        elif not(customer.email):
            error_message='enter your email'
        elif not(customer.password):
            error_message='eter a password'
        elif len(customer.password) <6:
            error_message="password must be 6 charecters long"
        elif customer.isExists():
            error_message="email already in use"

            return error_message

# login logic


class Login(View):
    return_url = None
    def get(self , request):
        Login.return_url = request.GET.get('return_url')
        return render(request , 'login.html')

    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('/')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)
        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect("/login")




# middleware for cart
# from django.shortcuts import redirect
#
# def auth_middleware(get_response):
#     # One-time configuration and initialization.
#
#     def middleware(request):
#         print(request.session.get('customer'))
#         returnUrl = request.META['PATH_INFO']
#         print(request.META['PATH_INFO'])
#         if not request.session.get('customer'):
#            return redirect(f'login?return_url={returnUrl}')
#
#         response = get_response(request)
#         return response
#
#     return middleware

# middleware for cart end

# cart here


class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = product.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )


# cart end
from testing.models import product

class checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        Products = product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, Products)

        for product1 in Products:
            print(cart.get(str(product1.id)))
            order1 = order(customer=Customer(id=customer),
                          product=product1,
                          price=product1.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product1.id)))
            order1.save()
        request.session['cart'] = {}

        return redirect('cart')


class Orders(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = order.get_orders_by_customer(customer)

        try:
            request.session['count'] += 1
        except:
            request.session['count'] = 0
        print(orders)
        return render(request, 'orders.html', {'orders': orders})





# def counter(request):
#     try:
#         request.session['count'] += 1
#     except:
#         request.session['count'] = 0
#
#     return render(request,'orders.html')
