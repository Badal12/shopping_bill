from app1.forms import LoginForm
from re import template
from django.contrib.auth.forms import AuthenticationForm
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views #for builtin login form import views builtin
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
urlpatterns = [
    #path('', views.home),
    path('', views.ProductView.as_view(),name='home'),
    #path('product-detail/', views.product_detail, name='product-detail'),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('buy/', views.buy_now, name='buy-now'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('mobile/', views.mobile, name='mobile'), #data = none in views.py so it will show all the mobile
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('checkout/', views.checkout, name='checkout'),

    #profile create class base url
    path('profile/', views.ProfileView.as_view(), name='profile'),

    #----------------Authentication urls below-----------------------------------------------------

    #path('login/', views.login, name='login'),  will use builtin views as auth_views and login form not forms.py form here
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app1/login.html', authentication_form=LoginForm), name='login'),

    #for logout we will be using the builtin logout class of django 
    #to redirect to again login page uese next_page=login
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), 

    #path('registration/', views.customerregistration, name='customerregistration'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),


    #we are using default-views as auth_view, form from forms.py, html file from template
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app1/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='changepassword'),

    #after change the password need to redirect where so write rul  usning default views
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='app1/passwordchangedone.html'), name='passwordchangedone'),

    #"password-reset templates--- 1.password-reset,2._reset_done,3.reset_confirm,4.reset_complete"

    # 1.when you forgot-password and want to reset it-- builtin view-auth_view, create form,create template
    #instead of sendig mail we can see the reset link in terminal fdo setting in settings.py
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='app1/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    
    #2.password_reset_done- above template redirect to done template
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app1/password_reset_done.html'), name='password_reset_done'),

     #3.password_reset_confirm- here we have to give and create form to user to reset the password after clickin on the link by mail
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='app1/password_reset_confirm.html', form_class = MySetPasswordForm), name='password_reset_confirm'),
    
    #4.password_reset_complete- it shwos the your pass reset ciis completed and rendering template confirm
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app1/password_reset_complete.html'), name='password_reset_complete'),


    #----------------end Authentication urls above-----------------------------------------------------
    #---------- now start creating add to cart product

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    #creating a new url for show_cart 
    path('cart/', views.show_cart, name='showcart'),
        
    path('pluscart/', views.plus_cart, name='pluscart'),






    #to show the images properly in browser which is stored from admin panel in db by seller need to do setting 
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)