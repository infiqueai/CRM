from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from .forms import YourRegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class CreateView(View):
    def get(self, request):
        return render(request, 'customer_relationship_management/create.html')

class ContactView(View):
    def get(self, request):
        return render(request, 'customer_relationship_management/contact.html')

class CreatetodolistView(View):
    def get(self, request):
        return render(request, 'customer_relationship_management/createtodolist.html')
    

class CreatedealView(View):
    def get(self, request):
        return render(request, 'customer_relationship_management/createdeal.html')    

class CreatecontactView(View):
    def get(self, request):
        return render(request, 'customer_relationship_management/createcontact.html')
    
class CreateclientView(View):
    def get(self, request):
        return render(request, 'customer_relationship_management/createclient.html')    


class CreatebillView(View):
    def get(self, request):
        return render(request, 'customer_relationship_management/createbill.html') 
       
class CreatedealView(View):
    def get(self, request):
        return render(request, 'customer_relationship_management/createdeal.html')

class CreatesellingView(View):
    def get(self, request):
        return render(request, 'customer_relationship_management/createselling.html')    
    
from .models import billInsert 
def billing(request):
    bills = billInsert.objects.all()  
    return render(request, 'customer_relationship_management/billing.html', {'bills': bills})

from .models import accInsert  
def client(request):
    accounts = accInsert.objects.all()  
    return render(request, 'customer_relationship_management/client.html', {'accounts': accounts})

def dashboard(request):
    return render(request, 'customer_relationship_management/dashboard.html')

from .models import dealInsert
def deal(request):
    deals = dealInsert.objects.all()  
    return render(request, 'customer_relationship_management/deal.html', {'deals': deals})


from .models import dealInsert, stdInsert

def lead(request):
    leads = stdInsert.objects.all()  # Fetch all records
    return render(request, 'customer_relationship_management/lead.html', {'leads': leads})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('customer_relationship_management:dashboard')
        else:
            messages.error(request, 'Invalid login credentials')

    return render(request, 'customer_relationship_management/login.html')

def register(request):
    if request.method == 'POST':
        form = YourRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('customer_relationship_management:login')
        else:
            messages.error(request, form.errors)
    else:
        form = YourRegistrationForm()

    return render(request, 'customer_relationship_management/register.html', {'form': form})

from .models import saleInsert  
def selling(request):
    sales = saleInsert.objects.all()  
    return render(request, 'customer_relationship_management/selling.html', {'sales': sales})

from .models import taskInsert  
def to_do_list(request):
    tasks = taskInsert.objects.all()  
    return render(request, 'customer_relationship_management/to_do_list.html', {'tasks': tasks})

from .models import conInsert  
def contact(request):
    contacts = conInsert.objects.all()  
    return render(request, 'customer_relationship_management/contact.html', {'contacts': contacts})

def leadtodeal(request, lead_id):
    lead_obj = stdInsert.objects.filter(id=lead_id).first()
    dealInsert.objects.update_or_create(
        dealowner = lead_obj.leadowner,
        leadsource = lead_obj.leadsource,
        exchangerate= lead_obj.exchangerate,
        numberofemployees= lead_obj.noofemp,
        turnover=lead_obj.annualrevenue,
        description= lead_obj.description,        
    )
    return lead(request)

def dealtobilling(request, deal_id):
    deal_obj = dealInsert.objects.filter(id=deal_id).first()
    billInsert.objects.update_or_create(
        invoiceowner = deal_obj.dealowner,
        accountname = deal_obj.accountname,
        contactname= deal_obj.contactname,
        dealname= deal_obj.dealname,
        currency=deal_obj.currency,
        amount=deal_obj.amount,
        description= deal_obj.description,        
    )
    return deal(request)

def contacttolead(request, contact_id):
    contact_obj = conInsert.objects.filter(id=contact_id).first()
    stdInsert.objects.update_or_create(
        # leadowner = request.user.username,
        leadowner = contact_obj.contactowner,
        leadsource = contact_obj.leadsource,
        firstname= contact_obj.firstname,
        lastname= contact_obj.lastname,
        title=contact_obj.title,
        mobile=contact_obj.mobile,
        email= contact_obj.email, 
        phone= contact_obj.phone,       
    )
    return contact(request)    

def dynamic_page_view(request, page_name):
    context = {'page_name': page_name}
    return render(request, 'dynamic_page_template.html', context)

from .forms import StdInsertForm
def Insertrecord(request):
    if request.method == 'POST':
        form = StdInsertForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record saved successfully..!')
            return redirect('customer_relationship_management:dashboard')
        else:
            messages.error(request, 'Record could not be saved.')
    
    else:
        form = StdInsertForm()

    return render(request, 'create.html', {'form': form})

from .forms import conInsertForm
def Fillrecord(request):
    if request.method == 'POST':
        form = conInsertForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record saved successfully..!')
            return redirect('customer_relationship_management:dashboard')
        else:
            messages.error(request, 'Record could not be saved.')
    
    else:
        form = conInsertForm()

    return render(request, 'createcontact.html', {'form': form})

from .forms import taskInsertForm
def Taskrecord(request):
    if request.method == 'POST':
        form = taskInsertForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record saved successfully..!')
            return redirect('customer_relationship_management:dashboard')
        else:
            messages.error(request, 'Record could not be saved.')
    
    else:
        form = taskInsertForm()

    return render(request, 'createtodolist.html', {'form': form})

from .forms import billInsertForm
def Billrecord(request):
    if request.method == 'POST':
        form = billInsertForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record saved successfully..!')
            return redirect('customer_relationship_management:dashboard')
        else:
            messages.error(request, 'Record could not be saved.')
    
    else:
        form = billInsertForm()

    return render(request, 'createbill.html', {'form': form})

from .forms import accInsertForm
def Accrecord(request):
    if request.method == 'POST':
        form = accInsertForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record saved successfully..!')
            return redirect('customer_relationship_management:dashboard')
        else:
            messages.error(request, 'Record could not be saved.')
    
    else:
        form = accInsertForm()

    return render(request, 'createclient.html', {'form': form})

from .forms import saleInsertForm
def Salerecord(request):
    if request.method == 'POST':
        form = saleInsertForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record saved successfully..!')
            return redirect('customer_relationship_management:dashboard')
        else:
            messages.error(request, 'Record could not be saved.')
    
    else:
        form = saleInsertForm()

    return render(request, 'createselling.html', {'form': form})

from .forms import dealInsertForm
def Dealrecord(request):
    if request.method == 'POST':
        form = dealInsertForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record saved successfully..!')
            return redirect('customer_relationship_management:dashboard')
        else:
            messages.error(request, 'Record could not be saved.')
    
    else:
        form = dealInsertForm()

    return render(request, 'createdeal.html', {'form': form})