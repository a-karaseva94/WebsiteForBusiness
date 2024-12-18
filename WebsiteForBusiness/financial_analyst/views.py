from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import *
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def main_page(request):
    """
        Возвращает пользователю шаблон "Главная страница"
    """
    return render(request, 'main_page.html')


def about_us(request):
    """
        Возвращает пользователю шаблон "О нас"
        text_about - текстовая информация в шаблон
    """
    text_about = ['Мы делаем бизнес-планы и финансовые модели для подачи заявки ',
                  'на получение льготного финансирования по программам ',
                  'федерального и регионального Фондов развития промышленности.']
    context = {
        'text_about': text_about,
    }
    return render(request, 'about_us.html', context)


def services(request):
    """
        Возвращает пользователю шаблон "Услуги"
        all_services - все услуги из модели услуги.
        Для отображения услуг встроен пагинатор (нумерация страниц)
    """
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
    """
        Функция для обработки post-запроса.
        Содержит форму для входа пользователя.
        Если пользователь зарегистрирован возвращает шаблон "Услуги",
        если нет - форму для регистрации.
        Если получает get-запрос, создает экземпляр формы для входа.
    """
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
    """
        Функция для обработки post-запроса.
        Содержит форму для регистрации пользователя.
        Если пользователь зарегистрирован, возвращает шаблон "Логин"
        Если получает get-запрос, создает экземпляр формы для регистрации.
    """
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
    """
        Функция для выхода из учетной записи.
        Если пользователь вышел, возвращает шаблон "Логин"
    """
    logout(request)
    return HttpResponseRedirect('/login')


@login_required
def cart(request):
    """
        Функция для модели Корзины:
        cart_items - все услуги из модели Корзины,
        total_cost - формула суммы для вычисления стоимости товаров в корзине.
        Возвращает пользователю шаблон "Корзина".
        Используется декоратор для ограничения доступа неавторизованным пользователям
    """
    cart_items = CartItem.objects.filter(user=request.user)
    total_cost = sum(item.service.cost * item.quantity for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_cost': total_cost
    }
    return render(request, 'cart.html', context)


@login_required
def add_to_cart(request, service_id):
    """
        Функция для добавления услуг в Корзину:
        service - все услуги из модели Услуг (присваивание id),
        cart_item, created - добавление услуг, выбранных пользователем, в корзину,
        cart_item.quantity - изменение количества услуг в корзине,
        cart_item.save - сохранение услуг в корзине.
        Возвращает пользователю шаблон "Корзина"
        Используется декоратор для ограничения доступа неавторизованным пользователям
    """
    service = Service.objects.get(id=service_id)
    cart_item, created = CartItem.objects.get_or_create(service=service,
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return HttpResponseRedirect('/cart')


def add_to_cart_yet(request, item_id):
    """
        Функция для увеличения количества одной и той же услуги в Корзину:
        cart_item - услуга, выбранная пользователем, в корзине,
        cart_item.quantity - увеличение количества услуги в корзине,
        cart_item.save - сохранение результата в корзине.
        Возвращает пользователю шаблон "Корзина"
    """
    cart_item = CartItem.objects.get(id=item_id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return HttpResponseRedirect('/cart')


def remove_from_cart(request, item_id):
    """
        Функция для удаления услуг из Корзины:
        cart_item - услуга, выбранная пользователем, в корзине,
        условие: если услуга в корзине одна - удаляется полностью,
        если нет - то удаление по одной.
        Возвращает пользователю шаблон "Корзина"
    """
    cart_item = CartItem.objects.get(id=item_id, user=request.user)
    if cart_item.quantity <=1:
        cart_item.delete()
    else:
        cart_item.quantity -= 1
        cart_item.save()
    return HttpResponseRedirect('/cart')
