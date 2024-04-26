from django.shortcuts import render, redirect
from django.contrib.auth import login   
from django.contrib.auth.decorators import login_required 
from django.db.models import Q

from product.models import Product, Company

from .forms import SignUpForm

# Create your views here.
def frontpage(request):
    products = Product.objects.all()[0:8]
    return render(request, 'core/frontpage.html', {'products': products})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()        
    return render(request, 'core/signup.html', {'form': form})

@login_required
def myaccount(request):
    return render(request, 'core/myaccount.html')

@login_required
def edit_myaccount(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.save()

        return redirect('myaccount')
    return render(request, 'core/edit_myaccount.html')

def shop(request):
    companies = Company.objects.all()
    products = Product.objects.all()

    active_company = request.GET.get('company', '')

    if active_company:
        products = products.filter(company__slug=active_company)

    query = request.GET.get('query', '')

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'companies': companies,
        'products': products,
        'active_company': active_company,
    }
    return render(request, 'core/shop.html', context)