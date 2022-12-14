from .models import Hall, Dish
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views import View
from .forms import OrderForm


def home(request):
    dishes = Dish.objects.all()
    halls = Hall.objects.all()

    return render(request, 'index.html', {'dishes': dishes, 'halls': halls})


def order(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Спасибо за заказ!')
    return render(request, 'order.html', {'form': form})


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html', {'form': UserCreationForm()})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        return render(request, 'register.html', {'form': form})
