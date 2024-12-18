from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import *
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def main_page(request):
    return render(request, 'main_page.html')


def about_us(request):
    text_about = ['Мы делаем бизнес-планы и финансовые модели для подачи заявки ',
                  'на получение льготного финансирования по программам ',
                  'федерального и регионального Фондов развития промышленности.']
    context = {
        'text_about': text_about,
    }
    return render(request, 'about_us.html', context)


# Пагинатор
def services(request):
    all_services = Service.objects.all().order_by('-id')
    per_page = request.GET.get('per_page', 2)
    paginator = Paginator(all_services, per_page)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    context = {
        'page_obj': page_obj,
        'per_page': per_page,
        'all_services': all_services,
    }
    return render(request, 'services.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/services')
            if user is None:
                return HttpResponseRedirect('/register')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return HttpResponseRedirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'registrate.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')

@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_cost = sum(item.service.cost * item.quantity for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_cost': total_cost
    }
    return render(request, 'cart.html', context)

@login_required
def add_to_cart(request, service_id):
    service = Service.objects.get(id=service_id)
    cart_item, created = CartItem.objects.get_or_create(service=service,
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return HttpResponseRedirect('/cart')


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id, user=request.user)
    cart_item.delete()
    return HttpResponseRedirect('/cart')
