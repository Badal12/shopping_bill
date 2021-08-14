from django import views
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from . models import Customer, Product, Cart, OrderPlaced
from . forms import CustomerRegistrationForm, CustomerProfileForm  #will import the form for userregistration
from django.contrib import messages #import for to show msg successfully registered
from django.db.models import Q
from django.http import JsonResponse

'''here we are rendering the home.html and we are gone write the 
logic of filtering the bottom-wear product, mobile product, etc and we are gonna pass 
it using for loop inside the home.html
'''
#def home(request):
# return render(request, 'app/home.html')
#-we are gona create the class base view of home.html--Product view
'''
on the base on category we are gonna filter it from db of models created field
filter the product according to category and put into perticular field
'''
class ProductView(View):
 def get(self, request):
  topwears = Product.objects.filter(category='TW')
  bottomwears = Product.objects.filter(category='BW')
  mobiles = Product.objects.filter(category='M')
  return render(request, 'app1/home.html', {'topwears': topwears, 'bottomwears': bottomwears, 'mobiles': mobiles})
#now we will pass this filter thorough context through dictionaryin the home.html file can print using for loop
'''
when we click on any product we should get all the details with unique id of product
for that we will have to write the class base view and same as have to pass the that to html file
'''

#def product_detail(request):
 #return render(request, 'app1/productdetail.html')

class ProductDetailView(View):
 def get(self, request, pk):
  product = Product.objects.get(pk=pk) #from db will fetch the id and assign to it
  return render(request, 'app1/productdetail.html', {'product': product}) #here we have to change the .html


def buy_now(request):
 return render(request, 'app1/buynow.html')


def change_password(request):
 return render(request, 'app/changepassword.html')

#def mobile(request):
# return render(request, 'app1/mobile.html')

def mobile(request, data=None): #when this data will come then only below logic will work.how can we pass that data
 #basically we can pass the data by url
 if data == None: #None means data nhi aa raha hai
     mobiles = Product.objects.filter(category='M') #then it will filter all mobiles category
 elif data == 'Redmi' or data == 'Samsung':
     mobiles = Product.objects.filter(category='M').filter(brand=data)
 elif data == 'below':
    mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=10000)
 elif data == 'above':
    mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=10000)
 return render(request, 'app1/mobile.html', {'mobiles': mobiles})


#def customerregistration(request):
# return render(request, 'app1/customerregistration.html')

class CustomerRegistrationView(View):
 def get(self, request):
     form = CustomerRegistrationForm()
     return render(request, 'app1/customerregistration.html', {'form': form})
 #if form comes with data then post() will called
 def post(self, request):
     form = CustomerRegistrationForm(request.POST)
     if form.is_valid():
         messages.success(request, 'congratulations!! Registered Successfully ')
         form.save()
     return render(request, 'app1/customerregistration.html', {'form': form})


def resetpassword(request):
    return render(request, 'app1/password_reset.html')

#no need of views for login bcoz we will use default django login form
 #def login(request): 
   # return render(request, 'app1/login.html')
#def profile(request):
# return render(request, 'app1/profile.html')

#creating view for profile to save the address in db need to create a modelform and urls and templates
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app1/profile.html', {'form':form, 'active':'btn-primary'}) #here when customer onclick in profile and address then that must be active so pass theat btn-primary here

    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city'] 
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request,'congratulation!! profile updated successfully')

        return render(request, 'app1/profile.html', {'form':form, 'active':'btn-primary'})

#to show the saved address into address fiel of profile write down the below 
def address(request):
    add = Customer.objects.filter(user=request.user) #if you want current user use request.user
    return render(request, 'app1/address.html', {'add':add, 'active':'btn-primary'})

#here we have to going to save thedata wht data in cart 
#1st-we have product id which product is addedd to cart for buy
#2nd which user selected a product to cart- want user
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    #now take the instance of product from product table db
    product = Product.objects.get(id=product_id)
    #now add to cart both user and product
    Cart(user=user, product=product).save()
    return redirect('/cart')

#instead of creating object in above def creating a ned def showcart
#here creating a object of cart that saves the data and render it will show all thedata
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user #will get the user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]#will get the product of authenticated user
        if cart_product: #if the user has the addedd the product to cart then 
            for p in cart_product: #all the product will come in p of all the product added and 
                tempamount = (p.quantity * p.product.discounted_price) #multiply the quantity * discounted price
                amount +=tempamount 
                totalamount = amount + shipping_amount
            return render(request, 'app1/addtocart.html', {'carts':cart, 'totalamount':totalamount, 'amount':amount})
        else:
            return render(request, 'app1/emptycart.html')

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id'] #below compare theid got from ajax and the login user id both condin must true
        print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        #recalculate the price after  increasing the product
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount +=tempamount
            #now pass the above data into ajax create var data 
            data = {
                'quantity': c.quantity,
                'amount': amount,
                'totalamount': amount + shipping_amount
            }
            return JsonResponse(data)

#for minus button logic belwo
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id'] #below compare theid got from ajax and the login user id both condin must true
        print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        #recalculate the price after  increasing the product
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount +=tempamount
            #now pass the above data into ajax create var data 
            data = {
                'quantity': c.quantity,
                'amount': amount,
                'totalamount': amount + shipping_amount
            }
            return JsonResponse(data)

#for remove button logic belwo
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id'] #below compare theid got from ajax and the login user id both condin must true
        print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        #recalculate the price after  deleting the product
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount +=tempamount
            #now pass the above data into ajax create var data 
            data = {
                'amount': amount,
                'totalamount': amount +shipping_amount,
            }
            return JsonResponse(data)



#----------------after product added to the cart ----now place the order --render the checkout ---view will create
#we need 2 things 1.cust address 2.product details 3.total amt toshwo in checkout

def checkout(request):
    user = request.user
    addres = Customer.objects.filter(user= user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    totalamount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:  #if the cart has some product then only we will calculate the totalamt
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        totalamount = amount + shipping_amount
    return render(request, 'app1/checkout.html', {'addres':addres, 'totalamount':totalamount, 'cart_items':cart_items})



#now show the datainto orderpalced  template that allthe detail regarding order placed
def orders(request):
    #retrive the data from  orderplaced db table whatever the data is placed by theuse is stored into that table and display inot order.html
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app1/orders.html', {'order_placed':op}) #pass the all the data which is inside the op var into template

#what are the things required in order_placed db table are check in db tablw and then retrive the data nad save it
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid') #this custid got it in checkout.html 
    customer = Customer.objects.get(id= custid) #retriving customer object from customer db table
    cart = Cart.objects.filter(user=user) #all the datais filtering from cart saving into cart variable
    for c in cart:  #the for loop will loop for every product and save the data of every produvt
        #saving data into orderplaced db table and ofter that data is deleting from cart
        OrderPlaced(user=user, customer=customer, product = c.product, quantity = c.quantity).save()
        c.delete() #after saving data into deleter it from cart
        return redirect("orders") #it will redirect to the below view 




































