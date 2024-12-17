from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import request

#from .forms import UserRegister
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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


def cart(request):
    return render(request, 'cart.html')


def login_or_registration(request):
    return render(request, 'login_or_registration.html')

# Регистрация
# def sign_up_by_django(request):
#     buyers = Buyer.objects.all()
#     users = [i.name for i in buyers]
#     info = {}
#     form = UserRegister()
#     context = {
#         'info': info,
#         'form': form,
#         'users': users,
#     }
#     if request.method == 'POST':
#         form = UserRegister(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             repeat_password = form.cleaned_data['repeat_password']
#             age = form.cleaned_data['age']
#             if password == repeat_password and int(age) >= 18 and username not in users:
#                 Buyer.objects.create(name=username, balance=0, age=age)
#                 return HttpResponse(f"Приветствуем, {username}!")
#             if password != repeat_password:
#                 info.update({'error1': 'Пароли не совпадают'})
#             if int(age) < 18:
#                 info.update({'error2': 'Вы должны быть старше 18'})
#             if username in users:
#                 info.update({'error3': 'Пользователь уже существует'})
#         else:
#             form = UserRegister()
#     return render(request, 'registration_page.html', context)
#
