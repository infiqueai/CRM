from django.urls import path
from .views import CreatetodolistView, CreatecontactView,CreatebillView, CreateclientView, CreatesellingView, CreatedealView, CreateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from . import views

app_name = 'customer_relationship_management'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('billing/', views.billing, name='billing'),
    path('client/', views.client, name='client'),
    path('contact/', views.contact, name='contact'),
    path('lead/', views.lead, name='lead'),
    path('deal/', views.deal, name='deal'),
    path('', LoginView.as_view(template_name='customer_relationship_management/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('create/', CreateView.as_view(), name='create'),
    path('createtodolist/', CreatetodolistView.as_view(), name='createtodolist'),
    path('createdeal/', CreatedealView.as_view(), name='createdeal'),
    path('createcontact/', CreatecontactView.as_view(), name='createcontact'),
    path('createselling/', CreatesellingView.as_view(), name='createselling'),
    path('createclient/', CreateclientView.as_view(), name='createclient'),
    path('createbill/', CreatebillView.as_view(), name='createbill'),
    path('selling/', views.selling, name='selling'),
    path('to_do_list/', views.to_do_list, name='to_do_list'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('Insertrecord', views.Insertrecord, name='Insertrecord'),
    path('Fillrecord', views.Fillrecord, name='Fillrecord'),
    path('Taskrecord', views.Taskrecord, name='Taskrecord'),
    path('Billrecord', views.Billrecord, name='Billrecord'),
    path('Accrecord', views.Accrecord, name='Accrecord'),
    path('Salerecord', views.Salerecord, name='Salerecord'),
    path('Dealrecord', views.Dealrecord, name='Dealrecord'),
    path( 'leadtodeal/<int:lead_id>/',views.leadtodeal, name='leadtodeal'),
    path( 'dealtobilling/<int:deal_id>/',views.dealtobilling, name='dealtobilling'),
    path( 'contacttolead/<int:contact_id>/',views.contacttolead, name='contacttolead'),
    path('<str:page_name>/', views.dynamic_page_view, name='dynamic_page'),
  

]
