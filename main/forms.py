from .models import Order
from django import forms


class OrderForm(forms.ModelForm):
    date = forms.CharField(help_text='В формате ГГГГ-ММ-ДД')

    class Meta:
        model = Order
        fields = '__all__'
